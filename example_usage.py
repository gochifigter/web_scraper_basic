"""
Example usage of the web scraper
"""
from scraper import WebScraper
from data_handler import DataHandler

def scrape_example_website():
    """
    Example function to scrape data from a sample website
    """
    # Initialize scraper and data handler
    scraper = WebScraper(delay=2)  # 2 second delay between requests
    data_handler = DataHandler()
    
    # Target URL (using a sample website for demonstration)
    url = "https://httpbin.org/html"
    
    # Fetch the page
    soup = scraper.fetch_page(url)
    
    if soup:
        # Extract data
        text_content = scraper.extract_text(soup, selector='div')
        metadata = scraper.extract_metadata(soup)
        links = scraper.extract_links(soup, url)
        
        # Prepare data for saving
        scraped_data = {
            'url': url,
            'metadata': metadata,
            'text_content': text_content,
            'links_found': links,
            'timestamp': str(scraper.session.timestamp if hasattr(scraper.session, 'timestamp') else 'N/A')
        }
        
        # Save data in different formats
        json_file = data_handler.save_json(scraped_data, 'example_data.json')
        text_file = data_handler.save_text(text_content, 'example_text.txt')
        
        print(f"Data saved to:")
        print(f"JSON: {json_file}")
        print(f"Text: {text_file}")
        print(f"Extracted {len(links)} links")
        
        return scraped_data
    else:
        print("Failed to fetch the page")
        return None

def scrape_multiple_pages():
    """
    Example function to scrape multiple pages
    """
    scraper = WebScraper(delay=1)
    data_handler = DataHandler()
    
    # List of URLs to scrape
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json"
    ]
    
    all_data = []
    
    for url in urls:
        print(f"Scraping: {url}")
        soup = scraper.fetch_page(url)
        
        if soup:
            data = {
                'url': url,
                'title': scraper.extract_text(soup, 'title'),
                'metadata': scraper.extract_metadata(soup),
                'timestamp': str(scraper.session.timestamp if hasattr(scraper.session, 'timestamp') else 'N/A')
            }
            all_data.append(data)
    
    # Save all data
    if all_data:
        csv_file = data_handler.save_csv(all_data, 'multiple_pages.csv')
        print(f"Multiple pages data saved to: {csv_file}")
    
    return all_data

if __name__ == "__main__":
    print("=== Single Page Scraping Example ===")
    scrape_example_website()
    
    print("\n=== Multiple Pages Scraping Example ===")
    scrape_multiple_pages()