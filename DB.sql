CREATE DATABASE hn_usage_data;

USE hn_usage_data;

CREATE TABLE usage_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    filter_type VARCHAR(50) NOT NULL,
    filtered_entries_count INT NOT NULL,
    crawled_entries_count INT NOT NULL,
    execution_duration DECIMAL(5, 2) NOT NULL
);
