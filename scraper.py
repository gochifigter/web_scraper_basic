"""
Main web scraper module with core functionality
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
    
    def fetch_page(self, url):
        """
        Fetch HTML content from a URL
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup: Parsed HTML content or None if failed
        """
        try:
            self.logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Respect rate limiting
            time.sleep(self.delay)
            
            return soup
            
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup, base_url, selector='a'):
        """
        Extract all links from a page
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            base_url (str): Base URL for relative links
            selector (str): CSS selector for links
            
        Returns:
            list: List of absolute URLs
        """
        links = []
        if soup:
            for link in soup.select(selector):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(base_url, href)
                    links.append(absolute_url)
        return links
    
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
            texts = [element.get_text(strip=True) for element in elements]
            return "\n".join(texts)
        else:
            return soup.get_text(strip=True)
    
    def extract_metadata(self, soup):
        """
        Extract metadata from HTML
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            
        Returns:
            dict: Metadata dictionary
        """
        metadata = {}
        
        if soup:
            # Title
            title_tag = soup.find('title')
            if title_tag:
                metadata['title'] = title_tag.get_text(strip=True)
            
            # Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                metadata['description'] = meta_desc.get('content', '')
            
            # All meta tags
            meta_tags = {}
            for meta in soup.find_all('meta'):
                name = meta.get('name') or meta.get('property')
                content = meta.get('content')
                if name and content:
                    meta_tags[name] = content
            metadata['meta_tags'] = meta_tags
        
        return metadata