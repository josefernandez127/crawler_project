import mysql.connector
from datetime import datetime

class DatabaseLogger:
    def __init__(self, config):
        self.config = config

    def _connect(self):
        return mysql.connector.connect(**self.config)

    def log_usage(self, filter_type, filtered_count, total_entries, duration):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        connection = self._connect()
        cursor = connection.cursor()

        query = '''
        INSERT INTO usage_logs (timestamp, filter_type, filtered_entries_count, crawled_entries_count, execution_duration)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (timestamp, filter_type, filtered_count, total_entries, duration))
        connection.commit()

        cursor.close()
        connection.close()
