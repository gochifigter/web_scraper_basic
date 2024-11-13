## Simple Web Scraper

A modular Python web scraper for extracting and saving data from websites.

### Features
- HTTP requests with proper headers and delays
- HTML parsing with BeautifulSoup
- Data extraction (titles, paragraphs, images, emails, tables)
- Multiple output formats (JSON, CSV, TXT)
- Configurable delays and timeouts
- Error handling and logging

### Installation

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

### Usage

1. **Basic single page scraping:**
```python
from scraper import WebScraper
from data_extractor import DataExtractor

scraper = WebScraper(delay=2)  # 2 second delay
soup = scraper.get_page("https://example.com")

if soup:
    titles = DataExtractor.extract_titles(soup)
    paragraphs = DataExtractor.extract_paragraphs(soup)
    print(f"Found {len(titles)} titles and {len(paragraphs)} paragraphs")
```

2. **Run the example:**
```bash
python main.py
```

3. **Customize for your needs:**
   - Modify `main.py` to target specific websites
   - Adjust selectors in `data_extractor.py`
   - Change output formats in `file_handler.py`

### File Structure
- `scraper.py` - Main scraping functionality
- `data_extractor.py` - Data extraction utilities
- `file_handler.py` - File saving utilities
- `main.py` - Example usage and demonstration
- `config.py` - Configuration settings
- `requirements.txt` - Required packages

### Important Notes

1. **Respect robots.txt** and website terms of service
2. **Use appropriate delays** to avoid overloading servers
3. **Check legality** of scraping target websites
4. **Handle errors gracefully** - websites may block scrapers
5. **Rotate user agents** if doing large-scale scraping

### Output
Scraped data is saved in the `output/` directory with timestamps:
- JSON files for structured data
- CSV files for tabular data
- TXT files for raw text

### Customization
- Modify CSS selectors in `DataExtractor` methods
- Add new extraction methods as needed
- Adjust delays and timeouts in `WebScraper` initialization
- Extend file formats in `FileHandler`

This scraper provides a solid foundation that you can extend for specific website structures and data requirements.