## Simple Web Scraper

A Python-based web scraper for extracting and saving data from websites.

### Features
- Extract text content from web pages
- Extract and filter links
- Save data in JSON, CSV, and text formats
- Configurable request delays and timeouts
- Error handling and logging

### Installation

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

### Usage

#### Method 1: Run the example
```bash
python main.py
```
This will scrape python.org and save the data in the `scraped_data` directory.

#### Method 2: Scrape a custom URL
```bash
python main.py --url "https://example.com" --output "my_data"
```

#### Method 3: Use in your own code
```python
from scraper import WebScraper
from data_handler import DataHandler

# Initialize components
scraper = WebScraper(delay=2)
data_handler = DataHandler()

# Scrape a website
soup = scraper.get_page("https://example.com")
if soup:
    text = scraper.extract_text(soup)
    links = scraper.extract_links(soup, "https://example.com")
    
    # Save data
    data_handler.save_text(text, "example.txt")
```

### File Structure
- `scraper.py` - Main scraping logic with WebScraper class
- `data_handler.py` - Data saving and file handling
- `main.py` - Example usage and command-line interface
- `config.py` - Configuration settings
- `requirements.txt` - Required Python packages

### Output
Data is saved in the `scraped_data` directory (configurable) with timestamps:
- JSON files for structured data
- CSV files for tabular data (like links)
- Text files for raw content

### Important Notes
- Always respect robots.txt and website terms of service
- Add delays between requests to avoid overloading servers
- Some websites may block automated requests
- Use responsibly and ethically

### Legal Considerations
- Only scrape publicly available data
- Respect copyright and terms of service
- Consider the website's bandwidth and resources
- Check if an API is available before scraping