"""
Main web scraper module
Handles HTTP requests and HTML parsing
"""
import requests
from bs4 import BeautifulSoup
import time
import logging
from urllib.parse import urljoin, urlparse

class WebScraper:
    def __init__(self, delay=1, timeout=10):
        """
        Initialize the web scraper
        
        Args:
            delay (int): Delay between requests in seconds
            timeout (int): Request timeout in seconds
        """
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def get_page(self, url):
        """
        Fetch a web page
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup: Parsed HTML content or None if failed
        """
        try:
            self.logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # Respect robots.txt and be polite
            time.sleep(self.delay)
            
            return BeautifulSoup(response.content, 'html.parser')
            
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup, base_url, filter_pattern=None):
        """
        Extract all links from a page
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            base_url (str): Base URL for relative links
            filter_pattern (str): Optional pattern to filter links
            
        Returns:
            list: List of absolute URLs
        """
        links = []
        if not soup:
            return links
            
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(base_url, href)
            
            # Filter links if pattern provided
            if filter_pattern and filter_pattern not in absolute_url:
                continue
                
            links.append(absolute_url)
            
        return list(set(links))  # Remove duplicates
    
    def extract_text(self, soup, selector=None):
        """
        Extract text content from HTML
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            selector (str): CSS selector to target specific elements
            
        Returns:
            str: Extracted text content
        """
        if not soup:
            return ""
            
        if selector:
            elements = soup.select(selector)
            text = ' '.join([elem.get_text(strip=True) for elem in elements])
        else:
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text(strip=True)
            
        return ' '.join(text.split())  # Clean up whitespace