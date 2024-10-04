## Simple Web Scraper

A modular Python web scraper for extracting and saving data from websites.

### Features

- **Modular Design**: Separate files for scraping, data extraction, and file writing
- **Polite Scraping**: Built-in delays between requests
- **Multiple Output Formats**: JSON, CSV, and plain text
- **Data Extraction**: Email addresses, phone numbers, tables, and metadata
- **Error Handling**: Robust error handling and logging

### Installation

1. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Basic Usage

Run the demo script:
```bash
python main.py
```

#### Custom Scraping

```python
from scraper import WebScraper
from data_extractor import DataExtractor
from file_writer import FileWriter

# Initialize scraper
scraper = WebScraper(delay=2)  # 2 second delay

# Scrape a page
url = "https://example.com"
soup = scraper.get_page(url)

if soup:
    # Extract data
    text = scraper.extract_text(soup)
    emails = DataExtractor.extract_emails(text)
    metadata = DataExtractor.extract_metadata(soup)
    
    # Save results
    data = {
        'url': url,
        'emails': emails,
        'metadata': metadata
    }
    FileWriter.save_json(data, 'scraped_data.json')
```

#### Scraping Multiple Pages

```python
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

scraper = WebScraper(delay=1)
all_data = []

for url in urls:
    soup = scraper.get_page(url)
    if soup:
        metadata = DataExtractor.extract_metadata(soup)
        all_data.append({
            'url': url,
            'title': metadata.get('title', '')
        })

FileWriter.save_csv(all_data, 'multiple_pages.csv')
```

### File Structure

- `scraper.py` - Main scraping functionality
- `data_extractor.py` - Data parsing and extraction utilities
- `file_writer.py` - File output handlers
- `main.py` - Example usage and demo
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies

### Output

The scraper creates an `output/` directory with:
- `scraped_data.json` - Structured data in JSON format
- `full_text.txt` - Raw text content
- `multiple_pages.csv` - Data from multiple pages (when used)

### Best Practices

1. **Respect robots.txt**: Check website's robots.txt before scraping
2. **Use delays**: Avoid overwhelming servers with rapid requests
3. **Handle errors**: Implement proper error handling for network issues
4. **Check legality**: Ensure you have permission to scrape the target website
5. **Use caching**: Consider caching responses to avoid repeated requests

### Legal Notice

Always ensure you have permission to scrape websites and comply with:
- Website Terms of Service
- robots.txt directives
- Copyright laws
- Data protection regulations (GDPR, CCPA, etc.)

This tool is for educational purposes. Use responsibly and ethically.