import unittest
from unittest.mock import patch, MagicMock
from crawler import NewsCrawler, NewsEntry
from database import DatabaseLogger

class TestNewsCrawler(unittest.TestCase):

    @patch('crawler.requests.get')
    def test_fetch_news_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
        <html>
            <a class="storylink">Test Title</a>
            <td class="subtext">
                <span class="score">100 points</span>
                <a>50 comments</a>
            </td>
        </html>
        '''
        mock_get.return_value = mock_response

        crawler = NewsCrawler()
        crawler.fetch_news()

        self.assertEqual(len(crawler.entries), 1)
        self.assertEqual(crawler.entries[0].title, "Test Title")
        self.assertEqual(crawler.entries[0].points, 100)
        self.assertEqual(crawler.entries[0].comments, 50)

    def test_word_count(self):
        entry = NewsEntry(1, "This is a test title", 100, 50)
        self.assertEqual(entry.word_count, 5)

    def test_filter_entries_more_than_five_words(self):
        crawler = NewsCrawler()
        crawler.entries = [
            NewsEntry(1, "This title has six words", 50, 10),
            NewsEntry(2, "Four words here", 100, 50)
        ]
        filtered = crawler.filter_entries('more_than_five_words')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "This title has six words")

    @patch('database.mysql.connector.connect')
    def test_log_usage(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        logger = DatabaseLogger(config={
            'host': 'localhost',
            'user': 'test_user',
            'password': 'test_password',
            'database': 'test_db'
        })
        logger.log_usage('more_than_five_words', 10, 30, 1.2)

        mock_conn.cursor().execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()
