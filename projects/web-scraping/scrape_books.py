# scrape_books.py
# Scrapes product information (title, price, rating, availability) from
# http://books.toscrape.com/ (a demo site made for scraping practice)
# and writes results to a CSV file.
import requests
from bs4 import BeautifulSoup
import csv
import argparse
import sys

def parse_rating(class_str):
    # class looks like "star-rating Three"
    parts = class_str.split()
    if len(parts) >= 2:
        return parts[1]
    return ""

def scrape_page(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    products = []
    for article in soup.select('article.product_pod'):
        title = article.h3.a['title'].strip()
        price = article.select_one('.price_color').text.strip()
        rating = parse_rating(article.select_one('.star-rating')['class'][1] if article.select_one('.star-rating') else "")
        availability = article.select_one('.availability').text.strip()
        products.append({
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability
        })
    return products

def get_page_url(base, page_num):
    if page_num == 1:
        return base
    return base.replace('index.html', '') + f'catalogue/page-{page_num}.html'

def main():
    parser = argparse.ArgumentParser(description='Scrape books.toscrape.com and save to CSV')
    parser.add_argument('--pages', type=int, default=1, help='Number of pages to scrape (default 1)')
    parser.add_argument('--output', type=str, default='books.csv', help='Output CSV filename')
    args = parser.parse_args()

    base = 'http://books.toscrape.com/index.html'
    all_products = []
    try:
        for p in range(1, args.pages + 1):
            url = get_page_url(base, p)
            print(f'Scraping {url} ...')
            products = scrape_page(url)
            if not products:
                print('No products found on page', p)
                break
            all_products.extend(products)
    except requests.RequestException as e:
        print('Network error:', e, file=sys.stderr)
        sys.exit(1)

    with open(args.output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title','price','rating','availability'])
        writer.writeheader()
        for row in all_products:
            writer.writerow(row)

    print(f'Done. Wrote {len(all_products)} products to {args.output}')

if __name__ == '__main__':
    main()
