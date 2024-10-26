import asyncio
import aiohttp
from selectolax.parser import HTMLParser
import re
import logging
from collections import defaultdict
import json


header = {
    "Cookie": "Seu Cookie aqui",
}
baseUrl = "https://aridesa.instructure.com"


async def fetch(session, url):
    async with session.get(url, headers=header) as response:
        return await response.text()


async def scrape_course(session, course, aridesaITA):
    courseTitle = course.text().strip()
    courseLink = f"{baseUrl}/{course.attrs.get('href')}"
    course_page = await fetch(session, courseLink)
    parser = HTMLParser(course_page)
    modules = parser.css(".module-item-title .ig-title.title.item_link")

    for module in modules:
        lectureTitle = module.attrs.get("title")

        if lectureTitle:
            lectureLink = module.attrs.get("href")
            lecture_page = await fetch(session, f"{baseUrl}{lectureLink}")
            videoUrlPattern = r"https://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)"
            match = re.search(videoUrlPattern, lecture_page)
            if match:
                ytLink = match.group(0)
                aridesaITA[courseTitle][lectureTitle] = lectureLink
                logging.info(f"Vídeo encontrado: {lectureTitle} - {ytLink}")
                continue
            logging.warning(f"Sem vídeo: {lectureTitle}")


async def main():
    aridesaITA = defaultdict(dict)
    async with aiohttp.ClientSession() as session:
        coursesUrl = f"{baseUrl}/courses"
        courses_page = await fetch(session, coursesUrl)
        parser = HTMLParser(courses_page)
        courses = parser.css("tbody a")

        tasks = [scrape_course(session, course, aridesaITA) for course in courses]
        await asyncio.gather(*tasks)

    with open("j.json", "w", encoding="UTF-8") as f:
        json.dump(aridesaITA, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    asyncio.run(main())
