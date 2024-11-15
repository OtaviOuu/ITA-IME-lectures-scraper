import asyncio
import aiohttp
from selectolax.parser import HTMLParser
import re
import logging
from collections import defaultdict
import json


header = {
    "Cookie": "_hp2_props.3001039959=%7B%22Base.appName%22%3A%22Canvas%22%7D; _hp2_id.3001039959=%7B%22userId%22%3A%22262276785038334%22%2C%22pageviewId%22%3A%227321202423762126%22%2C%22sessionId%22%3A%226914609638211522%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.3001039959=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1731643933972%2C%22d%22%3A%22sa.instructure.com%22%2C%22h%22%3A%22%2Flogin%2Fcanvas%22%7D; log_session_id=b2c2ca10069203c703b96a588730df6a; _legacy_normandy_session=TCKQ97mIybg_X1y1VOR6FQ+w-WPk0o5-nBbjgKKsQblxEcBLm2LoWRhHZtN4t2K3vXGcGr-w93OJnJ5Tnf3KtohLTbTXceGe7DMljJVmN9tDdZgMERW0sWr--Z8cbpiopGvV9hoB1d3hUxCxtTSKUJ53f5FNlaD9GJPqqlmFP00Ehz8pyyZLc_vD4pXU_YwIEGJd5vrGdMqWedCS1l5B07P-A79Y-9OSWJP-kxCEYvkkywDK4yJrg-fahpaP1jUhM6hI_h77v0S6azGk0RN4yEJEt7XTJjIN036Gd5oSM-X0_a6XrokCmVda6d8cuA-GeWowqtwCFnMVBR1JZrLboL6uEFVqbc07Le1w1gXarSIr4XBCN23MYZhNBiUEKp8pjj4iLsJEMrJrXvC0k6MNFeVKxBpy0RUu-QsVEaVw6ADnQ.y4OSlmGfzH2RM8NRXwnfhr5ycVY.ZzbKLA; canvas_session=TCKQ97mIybg_X1y1VOR6FQ+w-WPk0o5-nBbjgKKsQblxEcBLm2LoWRhHZtN4t2K3vXGcGr-w93OJnJ5Tnf3KtohLTbTXceGe7DMljJVmN9tDdZgMERW0sWr--Z8cbpiopGvV9hoB1d3hUxCxtTSKUJ53f5FNlaD9GJPqqlmFP00Ehz8pyyZLc_vD4pXU_YwIEGJd5vrGdMqWedCS1l5B07P-A79Y-9OSWJP-kxCEYvkkywDK4yJrg-fahpaP1jUhM6hI_h77v0S6azGk0RN4yEJEt7XTJjIN036Gd5oSM-X0_a6XrokCmVda6d8cuA-GeWowqtwCFnMVBR1JZrLboL6uEFVqbc07Le1w1gXarSIr4XBCN23MYZhNBiUEKp8pjj4iLsJEMrJrXvC0k6MNFeVKxBpy0RUu-QsVEaVw6ADnQ.y4OSlmGfzH2RM8NRXwnfhr5ycVY.ZzbKLA; _csrf_token=RzYnyDPARf4sF07CQ%2BATsee8xtkO0xPkD56wehr5UvwrX1TwdaF3xgd7Bvo3rCvGi968nG2DXJNs6%2FkVK5ZqyA%3D%3D",
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
