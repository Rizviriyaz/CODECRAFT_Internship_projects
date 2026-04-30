# Web Scraping Task - Example Project

This small project shows a working example of a web scraper that extracts product information (title, price, rating, availability)
from the demo e-commerce site **http://books.toscrape.com/** and saves the data as a CSV file.

## Files
- `scrape_books.py` - main scraper script (Python 3)
- `requirements.txt` - pip requirements
- `README.md` - this file

## Setup & Run
1. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scraper (example: scrape first 3 pages):
   ```bash
   python scrape_books.py --pages 3 --output books.csv
   ```
4. Open `books.csv` with Excel, LibreOffice or any text editor.

## Notes & legal
- This project uses `books.toscrape.com`, a site intended for learning scraping. When scraping other real websites, always check the site's Terms of Service and `robots.txt` and be respectful (rate-limit requests).
- This example focuses on clarity: you can extend it by adding pagination detection, retries, proxies, or using Scrapy / Selenium for JS-heavy sites.
