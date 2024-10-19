"""
Configuration settings for the web scraper
"""

# Default settings
DEFAULT_CONFIG = {
    'request_delay': 1,  # seconds between requests
    'timeout': 10,       # request timeout in seconds
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'output_directory': 'output',
    'max_retries': 3,
    'retry_delay': 5,
}

# Common CSS selectors for different types of content
SELECTORS = {
    'articles': 'article, .article, .post, .content',
    'headings': 'h1, h2, h3, h4, h5, h6',
    'paragraphs': 'p',
    'links': 'a',
    'images': 'img',
    'lists': 'ul, ol',
}