"""
Configuration settings for the web scraper
"""

# Default settings
DEFAULT_CONFIG = {
    "request_delay": 1,  # seconds between requests
    "timeout": 10,       # request timeout in seconds
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "output_directory": "scraped_data",
    "max_retries": 3
}

# Example URLs for testing
EXAMPLE_URLS = [
    "https://www.python.org",
    "https://httpbin.org/html",
    "https://httpbin.org/json"
]