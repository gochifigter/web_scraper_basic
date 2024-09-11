"""
Data extraction utilities for specific data types
"""
from bs4 import BeautifulSoup
import re

class DataExtractor:
    @staticmethod
    def extract_emails(text):
        """
        Extract email addresses from text
        
        Args:
            text (str): Text to search for emails
            
        Returns:
            list: List of email addresses found
        """
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, text)
    
    @staticmethod
    def extract_phone_numbers(text):
        """
        Extract phone numbers from text
        
        Args:
            text (str): Text to search for phone numbers
            
        Returns:
            list: List of phone numbers found
        """
        phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(phone_pattern, text)
    
    @staticmethod
    def extract_tables(soup):
        """
        Extract data from HTML tables
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            
        Returns:
            list: List of tables as lists of rows
        """
        tables = []
        for table in soup.find_all('table'):
            table_data = []
            for row in table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                if row_data:
                    table_data.append(row_data)
            if table_data:
                tables.append(table_data)
        return tables
    
    @staticmethod
    def extract_metadata(soup):
        """
        Extract meta tags information
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            
        Returns:
            dict: Dictionary of meta tag content
        """
        metadata = {}
        # Title
        title = soup.find('title')
        if title:
            metadata['title'] = title.get_text(strip=True)
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            metadata['description'] = meta_desc.get('content', '')
        
        # Meta keywords
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            metadata['keywords'] = meta_keywords.get('content', '')
        
        # Open Graph tags
        og_tags = soup.find_all('meta', attrs={'property': re.compile(r'^og:')})
        for tag in og_tags:
            key = tag.get('property', '').replace('og:', '')
            metadata[f'og_{key}'] = tag.get('content', '')
        
        return metadata