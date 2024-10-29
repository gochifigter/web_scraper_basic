"""
Data extraction utilities for common web scraping patterns
"""

from bs4 import BeautifulSoup
import re

class DataExtractor:
    @staticmethod
    def extract_titles(soup, title_selector='h1, h2, h3'):
        """
        Extract titles from HTML
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            title_selector (str): CSS selector for titles
            
        Returns:
            list: List of title texts
        """
        if not soup:
            return []
            
        titles = []
        for title in soup.select(title_selector):
            text = title.get_text(strip=True)
            if text:
                titles.append(text)
        return titles
    
    @staticmethod
    def extract_paragraphs(soup, paragraph_selector='p'):
        """
        Extract paragraphs from HTML
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            paragraph_selector (str): CSS selector for paragraphs
            
        Returns:
            list: List of paragraph texts
        """
        if not soup:
            return []
            
        paragraphs = []
        for p in soup.select(paragraph_selector):
            text = p.get_text(strip=True)
            if text and len(text) > 10:  # Filter very short paragraphs
                paragraphs.append(text)
        return paragraphs
    
    @staticmethod
    def extract_images(soup, base_url):
        """
        Extract image URLs from HTML
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            base_url (str): Base URL for relative image paths
            
        Returns:
            list: List of absolute image URLs
        """
        from urllib.parse import urljoin
        
        if not soup:
            return []
            
        images = []
        for img in soup.find_all('img', src=True):
            src = img['src']
            if not src.startswith(('http://', 'https://')):
                src = urljoin(base_url, src)
            images.append(src)
        return images
    
    @staticmethod
    def extract_emails(text):
        """
        Extract email addresses from text
        
        Args:
            text (str): Text to search for emails
            
        Returns:
            list: List of email addresses
        """
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, text)
    
    @staticmethod
    def extract_table_data(soup, table_selector='table'):
        """
        Extract data from HTML tables
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            table_selector (str): CSS selector for tables
            
        Returns:
            list: List of tables, each table is a list of rows
        """
        if not soup:
            return []
            
        tables_data = []
        for table in soup.select(table_selector):
            table_data = []
            for row in table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                if row_data:
                    table_data.append(row_data)
            if table_data:
                tables_data.append(table_data)
        return tables_data