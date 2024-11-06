"""
Main script demonstrating web scraper usage
"""

from scraper import WebScraper
from data_extractor import DataExtractor
from file_handler import FileHandler

def scrape_website_example():
    """
    Example usage of the web scraper
    """
    # Initialize scraper
    scraper = WebScraper(delay=2)  # 2 second delay between requests
    
    # Example URL (replace with your target website)
    url = "https://httpbin.org/html"  # Using a test URL
    
    # Fetch the page
    soup = scraper.get_page(url)
    
    if soup:
        # Extract various types of data
        titles = DataExtractor.extract_titles(soup)
        paragraphs = DataExtractor.extract_paragraphs(soup)
        images = DataExtractor.extract_images(soup, url)
        
        # Extract all text for email searching
        all_text = scraper.extract_text(soup)
        emails = DataExtractor.extract_emails(all_text)
        
        # Extract links
        links = scraper.extract_links(soup, url)
        
        # Prepare data for saving
        scraped_data = {
            'url': url,
            'titles': titles,
            'paragraphs': paragraphs,
            'images': images,
            'emails': emails,
            'links': links,
            'all_text': all_text[:500] + '...' if len(all_text) > 500 else all_text  # Preview
        }
        
        # Save data
        filename = FileHandler.generate_filename('example_scrape')
        FileHandler.save_json(scraped_data, filename)
        FileHandler.save_text(all_text, f"{filename}_full_text")
        
        # Print summary
        print(f"\nScraping Summary for {url}:")
        print(f"Titles found: {len(titles)}")
        print(f"Paragraphs found: {len(paragraphs)}")
        print(f"Images found: {len(images)}")
        print(f"Emails found: {len(emails)}")
        print(f"Links found: {len(links)}")
        
        return scraped_data
    else:
        print("Failed to fetch the page")
        return None

def scrape_multiple_pages(urls):
    """
    Example of scraping multiple pages
    """
    scraper = WebScraper(delay=1)
    all_data = []
    
    for url in urls:
        print(f"\nScraping: {url}")
        soup = scraper.get_page(url)
        
        if soup:
            data = {
                'url': url,
                'titles': DataExtractor.extract_titles(soup),
                'text_preview': scraper.extract_text(soup)[:200] + '...'
            }
            all_data.append(data)
    
    # Save combined data
    if all_data:
        FileHandler.save_json(all_data, 'multiple_pages_scrape')
        FileHandler.save_csv(all_data, 'multiple_pages_scrape')
    
    return all_data

if __name__ == "__main__":
    print("Starting web scraper example...")
    
    # Example 1: Single page scraping
    data = scrape_website_example()
    
    # Example 2: Multiple pages scraping (uncomment to use)
    # urls = [
    #     "https://httpbin.org/html",
    #     "https://httpbin.org/xml"
    # ]
    # multiple_data = scrape_multiple_pages(urls)
    
    print("\nWeb scraping completed!")