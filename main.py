"""
Main script to demonstrate web scraping functionality
"""
from scraper import WebScraper
from data_extractor import DataExtractor
from file_writer import FileWriter
import json

def scrape_website_example():
    """
    Example usage of the web scraper
    """
    # Initialize scraper
    scraper = WebScraper(delay=2)  # 2 second delay between requests
    
    # Example: Scrape a website
    url = "https://httpbin.org/html"  # Using a test URL
    soup = scraper.get_page(url)
    
    if soup:
        # Extract basic information
        text_content = scraper.extract_text(soup)
        links = scraper.extract_links(soup, url)
        metadata = DataExtractor.extract_metadata(soup)
        
        # Prepare data for saving
        scraped_data = {
            'url': url,
            'metadata': metadata,
            'links_found': len(links),
            'sample_links': links[:5],  # First 5 links
            'text_preview': text_content[:500] + "..." if len(text_content) > 500 else text_content
        }
        
        # Save data
        FileWriter.save_json(scraped_data, 'output/scraped_data.json')
        FileWriter.save_text(text_content, 'output/full_text.txt')
        
        print("Scraping completed successfully!")
        print(f"Found {len(links)} links")
        print(f"Page title: {metadata.get('title', 'N/A')}")
    
    else:
        print("Failed to fetch the page")

def scrape_multiple_pages(urls):
    """
    Example of scraping multiple pages
    
    Args:
        urls (list): List of URLs to scrape
    """
    scraper = WebScraper(delay=1)
    all_data = []
    
    for url in urls:
        print(f"Scraping: {url}")
        soup = scraper.get_page(url)
        
        if soup:
            metadata = DataExtractor.extract_metadata(soup)
            page_data = {
                'url': url,
                'title': metadata.get('title', ''),
                'description': metadata.get('description', ''),
                'scraped_at': str(scraper.session.get(url).elapsed)
            }
            all_data.append(page_data)
    
    # Save combined data
    if all_data:
        FileWriter.save_csv(all_data, 'output/multiple_pages.csv')
        print(f"Scraped data from {len(all_data)} pages")

if __name__ == "__main__":
    print("Simple Web Scraper Demo")
    print("=" * 30)
    
    # Example 1: Single page scraping
    scrape_website_example()
    
    # Example 2: Multiple pages (uncomment to use)
    # urls = [
    #     "https://httpbin.org/html",
    #     "https://httpbin.org/json"
    # ]
    # scrape_multiple_pages(urls)