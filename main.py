"""
Main script to demonstrate web scraping functionality
"""
from scraper import WebScraper
from data_handler import DataHandler
import argparse

def scrape_website_example():
    """
    Example function demonstrating web scraping
    """
    # Initialize components
    scraper = WebScraper(delay=2)  # 2 second delay between requests
    data_handler = DataHandler()
    
    # Example: Scrape Python.org
    url = "https://www.python.org"
    
    print(f"Scraping: {url}")
    soup = scraper.get_page(url)
    
    if soup:
        # Extract basic information
        title = soup.title.string if soup.title else "No title"
        text_content = scraper.extract_text(soup, selector="div.container")
        links = scraper.extract_links(soup, url, filter_pattern="python")
        
        # Prepare data for saving
        scraped_data = {
            "url": url,
            "title": title,
            "total_links_found": len(links),
            "sample_links": links[:5],  # First 5 links
            "text_preview": text_content[:500] + "..." if len(text_content) > 500 else text_content
        }
        
        # Save data in different formats
        data_handler.save_json(scraped_data, "python_org_data.json")
        data_handler.save_text(text_content, "python_org_text.txt")
        
        # Save links as CSV
        links_data = [{"url": link, "source": url} for link in links]
        data_handler.save_csv(links_data, "python_org_links.csv")
        
        print("Scraping completed successfully!")
        return scraped_data
    else:
        print("Failed to scrape the website")
        return None

def main():
    """
    Main function with command line interface
    """
    parser = argparse.ArgumentParser(description="Simple Web Scraper")
    parser.add_argument("--url", help="URL to scrape")
    parser.add_argument("--output", help="Output directory", default="scraped_data")
    
    args = parser.parse_args()
    
    if args.url:
        # Custom URL scraping
        scraper = WebScraper()
        data_handler = DataHandler(args.output)
        
        soup = scraper.get_page(args.url)
        if soup:
            title = soup.title.string if soup.title else "No title"
            text_content = scraper.extract_text(soup)
            
            data = {
                "url": args.url,
                "title": title,
                "content": text_content
            }
            
            data_handler.save_json(data, "custom_scrape.json")
            print(f"Scraped: {args.url}")
    else:
        # Run example
        scrape_website_example()

if __name__ == "__main__":
    main()