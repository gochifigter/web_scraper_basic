"""
Configuration settings for the web scraper
"""

# Default settings
DEFAULT_DELAY = 1  # seconds between requests
DEFAULT_TIMEOUT = 10  # request timeout in seconds
MAX_RETRIES = 3

# Output settings
OUTPUT_DIRECTORY = 'output'
LOG_LEVEL = 'INFO'

# User agent strings (rotate if needed)
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]