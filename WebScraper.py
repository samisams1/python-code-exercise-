import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Example: Extract all links
    links = [link.get('href') for link in soup.find_all('a')]
    return links

print(scrape_website("https://example.com"))