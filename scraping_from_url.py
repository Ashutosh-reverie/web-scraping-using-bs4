import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

import sys 
limit = sys.getrecursionlimit(10000)

lines=open(f"website_URLS_mai_02", 'r')
internal_urls=lines.readlines()
len(internal_urls)


for url in internal_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml', from_encoding='utf-8')
    try:
        title = soup.find('title').get_text()
    except AttributeError:
        continue
    paragraphs = soup.find_all('p')
    with open('web_Scraping_mai', mode = "a", encoding = "UTF-8") as file:
            for p in paragraphs:
                file.write(p.get_text())
                #print(p.get_text())
