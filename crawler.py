import requests
from bs4 import BeautifulSoup
import re
import time

class NewsEntry:
    def __init__(self, number, title, points, comments):
        self.number = number
        self.title = title
        self.points = points
        self.comments = comments
        self.word_count = self._count_words()

    def _count_words(self):
        clean_title = re.sub(r'[^a-zA-Z\s]', '', self.title)
        return len(clean_title.split())

class NewsCrawler:
    def __init__(self, url="https://news.ycombinator.com/", max_entries=30):
        self.url = url
        self.max_entries = max_entries
        self.entries = []

    def fetch_news(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the news: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all("a", class_="storylink")
        subtexts = soup.find_all("td", class_="subtext")

        for i, (title, subtext) in enumerate(zip(titles, subtexts)):
            if i >= self.max_entries:
                break
            entry = self._parse_entry(i + 1, title, subtext)
            self.entries.append(entry)

    def _parse_entry(self, number, title, subtext):
        points = self._extract_points(subtext)
        comments = self._extract_comments(subtext)
        return NewsEntry(number, title.get_text(), points, comments)

    def _extract_points(self, subtext):
        points = subtext.find("span", class_="score")
        return int(points.get_text().split()[0]) if points else 0

    def _extract_comments(self, subtext):
        comments = subtext.find_all("a")[-1].get_text()
        if "comment" in comments:
            return int(comments.split()[0]) if comments.split()[0] != "discuss" else 0
        return 0

    def filter_entries(self, filter_type):
        if filter_type == 'more_than_five_words':
            filtered = [entry for entry in self.entries if entry.word_count > 5]
            return sorted(filtered, key=lambda x: x.comments, reverse=True)
        elif filter_type == 'five_or_less_words':
            filtered = [entry for entry in self.entries if entry.word_count <= 5]
            return sorted(filtered, key=lambda x: x.points, reverse=True)
        else:
            raise ValueError("Invalid filter type")
