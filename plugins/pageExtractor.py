import requests
from bs4 import BeautifulSoup
import sys

def extract_text(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    for a in soup.find_all('a'):
        if a.string:
            a.string.replace_with(f"{a.string}[{a['href']}]")

    text = soup.get_text()

    return ' '.join(text.split())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    text = extract_text(url)
    print(text)
