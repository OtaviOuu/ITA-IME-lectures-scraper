# Aridesa Course Scraper

Asynchronous Python script to extract course information and videos from the Aridesa Instructure Canvas platform. The script maps the course structure and saves the information to a JSON file.

## Features

- Asynchronous data extraction
- Complete mapping of courses and lectures
- Automatic YouTube video detection
- JSON export
- Progress logging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OtaviOuu/ITA-IME-ArideS-Downloader
cd aridesa-scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Copy the environment example file:
```bash
cp .env.example .env
```

2. Get the authentication cookie:
   - Go to https://aridesa.instructure.com/courses
   - Login if necessary
   - Open Developer Tools (F12)
   - Go to Network tab
   - Refresh the page
   - Look for "courses" in the requests
   - In Headers > Request Headers, copy the cookie value
   - Paste it into the `.env` file

## Usage

Run the script:
```bash
python src/main.py
```

The script will:
1. Access all available courses
2. Extract lecture information
3. Detect YouTube videos
4. Generate a `j.json` file with the structure:
```json
{
    "Course Name": {
        "Lecture Title": "Lecture Link",
        ...
    },
    ...
}
```

## Project Structure
```
.
├── README.md
├── requirements.txt
└── src
    └── main.py
```

## Dependencies

- aiohttp: Asynchronous HTTP requests
- selectolax: HTML Parser
- python-dotenv: Environment variables management

## Notes

- Active login required on Aridesa platform
- Cookie expires periodically and needs to be updated
- Use responsibly following platform's terms of use

## Responsibility Statement

This tool is provided for educational purposes only. Users are responsible for:

- Obtaining proper authorization before accessing any content
- Using the tool in accordance with Aridesa's terms of service
- Not distributing or sharing downloaded content
- Ensuring compliance with institutional policies
- Using the extracted data ethically and legally

The developer(s) assume no liability for misuse of this tool or violation of terms of service. Use at your own discretion and responsibility.
