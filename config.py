"""
Configuration settings for the web scraper
"""
# Request settings
DEFAULT_DELAY = 1  # seconds between requests
DEFAULT_TIMEOUT = 10  # request timeout in seconds

# Output settings
OUTPUT_DIR = "output"
DEFAULT_OUTPUT_FORMAT = "json"

# User agent to mimic real browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Allowed file formats
SUPPORTED_FORMATS = ['json', 'csv', 'txt']