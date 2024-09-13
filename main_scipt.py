from crawler import NewsCrawler
from database import DatabaseLogger
import time

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'hn_usage_data'
}

if __name__ == "__main__":
    crawler = NewsCrawler()
    logger = DatabaseLogger(config=db_config)

    # Timing the process
    start_time = time.time()

    # Fetch news entries
    crawler.fetch_news()

    # Filter by titles with more than five words, ordered by comments
    filtered_entries = crawler.filter_entries('more_than_five_words')

    # Measure the execution duration
    end_time = time.time()
    duration = end_time - start_time

    # Log the result in the database
    logger.log_usage('more_than_five_words', len(filtered_entries), len(crawler.entries), duration)

    # Output the filtered entries
    for entry in filtered_entries:
        print(f"{entry.number}: {entry.title} | {entry.points} points | {entry.comments} comments")
