## Simple Web Scraper

A Python-based web scraper that extracts and saves data from websites.

### Installation

1. Clone or download the files to your local directory
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Files Structure

- `scraper.py` - Main scraping logic with WebScraper class
- `data_handler.py` - Data storage and export functionality
- `main.py` - Example usage and command-line interface
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies

### Usage

#### Method 1: Run Example (Recommended for testing)
```bash
python main.py
```
This scrapes quotes from quotes.toscrape.com and saves them as JSON and CSV.

#### Method 2: Custom Scraping
```bash
# Scrape specific URL and save as JSON
python main.py --url "https://example.com" --format json

# Scrape with CSS selector
python main.py --url "https://example.com" --selector ".article-title" --format csv

# Save as text file
python main.py --url "https://example.com" --format txt
```

#### Method 3: Use in Your Code
```python
from scraper import WebScraper
from data_handler import DataHandler

# Initialize
scraper = WebScraper(delay=1)
data_handler = DataHandler()

# Scrape a page
soup = scraper.get_page("https://example.com")

# Extract specific content
titles = soup.select("h1, h2, h3")
data = [{"text": title.get_text(strip=True)} for title in titles]

# Save results
data_handler.save_to_json(data, "results.json")
```

### Features

- **Respectful Scraping**: Built-in delays between requests
- **Multiple Output Formats**: JSON, CSV, and plain text
- **CSS Selector Support**: Target specific page elements
- **Error Handling**: Robust error handling for network issues
- **Duplicate Removal**: Automatic removal of duplicate links
- **Configurable**: Easy to customize delays, timeouts, and output

### Output

All output files are saved in the `output/` directory with timestamps.

### Important Notes

1. **Respect robots.txt**: Always check a website's robots.txt file before scraping
2. **Rate Limiting**: The scraper includes delays to avoid overwhelming servers
3. **Legal Compliance**: Ensure you have permission to scrape the target website
4. **Dynamic Content**: This scraper works with static HTML (not JavaScript-rendered content)

### Example Output Formats

**JSON:**
```json
[
  {
    "text": "The world as we have created it is a process of our thinking...",
    "author": "Albert Einstein",
    "tags": ["change", "deep-thoughts", "thinking", "world"],
    "url": "http://quotes.toscrape.com"
  }
]
```

**CSV:**
```csv
text,author,tags,url
"The world as we have created it...",Albert Einstein,"['change', 'deep-thoughts', 'thinking', 'world']",http://quotes.toscrape.com
```