
# Hacker News Crawler

## Overview
This project is a Python-based web crawler that extracts the top 30 entries from [Hacker News](https://news.ycombinator.com/) and provides functionality to filter and log usage data. The project follows clean code principles, is thoroughly tested, and supports logging in a MySQL database.

## Features
- Extracts the first 30 news entries from Hacker News.
- Filters entries based on the number of words in the title:
    - More than 5 words, sorted by comments.
    - 5 words or fewer, sorted by points.
- Logs usage data into a MySQL database.

## Project Structure
hn_crawler/
    crawler.py # Core functionality
    database.py # DB connection and logging
    DB.sql # DB creation
    tests/ # Automated tests
        test_crawler.py
    main_script.py # Main functionality
    README.md # Project documentation
    requirements.txt # Dependencies

## Setup

1. Install the required dependencies:

   pip install -r requirements.txt
