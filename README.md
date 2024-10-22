## Simple Web Scraper

A Python-based web scraper for extracting and saving data from websites.

### Installation

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Files Overview

- **`scraper.py`** - Main scraper class with core functionality
- **`data_handler.py`** - Data storage and export utilities
- **`example_usage.py`** - Example implementations
- **`config.py`** - Configuration settings
- **`requirements.txt`** - Python dependencies

### Basic Usage

1. **Import and initialize the scraper:**
   ```python
   from scraper import WebScraper
   from data_handler import DataHandler
   
   scraper = WebScraper(delay=2)  # 2-second delay between requests
   data_handler = DataHandler()
   ```

2. **Fetch and extract data:**
   ```python
   url = "https://example.com"
   soup = scraper.fetch_page(url)
   
   if soup:
       # Extract text content
       text = scraper.extract_text(soup, selector='.content')
       
       # Extract metadata
       metadata = scraper.extract_metadata(soup)
       
       # Extract links
       links = scraper.extract_links(soup, url)
   ```

3. **Save extracted data:**
   ```python
   # Save as JSON
   data_handler.save_json({'content': text, 'metadata': metadata}, 'data.json')
   
   # Save as CSV (for multiple items)
   data_handler.save_csv([{'url': url, 'text': text}], 'data.csv')
   
   # Save as text
   data_handler.save_text(text, 'content.txt')
   ```

### Running Examples

Run the example script to see the scraper in action:
```bash
python example_usage.py
```

### Features

- **Rate Limiting**: Configurable delays between requests
- **Error Handling**: Robust error handling for network issues
- **Multiple Output Formats**: JSON, CSV, and text file support
- **Metadata Extraction**: Automatically extracts page metadata
- **Link Extraction**: Finds and normalizes all links on a page
- **Configurable**: Easy to customize request headers, timeouts, etc.

### Important Notes

- **Respect robots.txt**: Always check website's robots.txt before scraping
- **Rate Limiting**: Use appropriate delays to avoid overwhelming servers
- **Legal Compliance**: Ensure you have permission to scrape target websites
- **User Agent**: Uses a standard browser user agent by default

### Customization

Modify `config.py` to adjust default settings or add custom CSS selectors for specific websites.

### Error Handling

The scraper includes comprehensive error handling for:
- Network timeouts
- HTTP errors
- Invalid URLs
- Parser errors