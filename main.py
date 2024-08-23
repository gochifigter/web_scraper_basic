"""
Main script to run the web scraper
Example usage and demonstration
"""
from scraper import WebScraper
from data_handler import DataHandler
import argparse

def scrape_example_website():
    """
    Example: Scrape quotes from quotes.toscrape.com
    """
    print("Starting web scraper example...")
    
    # Initialize components
    scraper = WebScraper(delay=1)
    data_handler = DataHandler()
    
    base_url = "http://quotes.toscrape.com"
    scraped_data = []
    
    # Scrape the first page
    soup = scraper.get_page(base_url)
    
    if soup:
        # Extract quotes
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text_elem = quote.find('span', class_='text')
            author_elem = quote.find('small', class_='author')
            tags_elems = quote.find_all('a', class_='tag')
            
            quote_data = {
                'text': text_elem.get_text(strip=True) if text_elem else '',
                'author': author_elem.get_text(strip=True) if author_elem else '',
                'tags': [tag.get_text(strip=True) for tag in tags_elems],
                'url': base_url
            }
            scraped_data.append(quote_data)
        
        # Save results
        json_file = data_handler.save_to_json(scraped_data, "quotes.json")
        csv_file = data_handler.save_to_csv(scraped_data, "quotes.csv")
        
        print(f"Scraped {len(scraped_data)} quotes")
        print(f"JSON output: {json_file}")
        print(f"CSV output: {csv_file}")
        
        # Display first few results
        print("\nFirst 3 quotes:")
        for i, quote in enumerate(scraped_data[:3]):
            print(f"{i+1}. {quote['text']} - {quote['author']}")

def custom_scrape(url, selector=None, output_format='json'):
    """
    Custom scraping function for any website
    
    Args:
        url (str): URL to scrape
        selector (str): CSS selector for specific content
        output_format (str): Output format ('json', 'csv', 'txt')
    """
    scraper = WebScraper(delay=2)
    data_handler = DataHandler()
    
    soup = scraper.get_page(url)
    
    if soup:
        if selector:
            # Extract specific elements
            elements = soup.select(selector)
            extracted_data = []
            
            for elem in elements:
                extracted_data.append({
                    'text': elem.get_text(strip=True),
                    'html': str(elem),
                    'url': url
                })
            
            if output_format == 'json':
                data_handler.save_to_json(extracted_data, "custom_scrape.json")
            elif output_format == 'csv':
                data_handler.save_to_csv(extracted_data, "custom_scrape.csv")
                
        else:
            # Extract all text
            text = scraper.extract_text(soup)
            data_handler.save_to_txt(text, "full_page_text.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple Web Scraper')
    parser.add_argument('--url', help='URL to scrape')
    parser.add_argument('--selector', help='CSS selector for specific content')
    parser.add_argument('--format', choices=['json', 'csv', 'txt'], 
                       default='json', help='Output format')
    
    args = parser.parse_args()
    
    if args.url:
        # Custom scraping
        custom_scrape(args.url, args.selector, args.format)
        print(f"Scraped {args.url} and saved results to output/ directory")
    else:
        # Run example
        scrape_example_website()