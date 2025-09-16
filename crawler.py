import requests
import re
from urllib.parse import urljoin
url = input("Enter the URL: ")
visted_links =[]
def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.text))
def crawl(url):
    href_links = extract_links(url)
    for link in href_links:
        link = urljoin(url, link)
        if url in link and link not in visted_links:
            visted_links.append(link)
            print(link)
            crawl(url)
crawl(url)
