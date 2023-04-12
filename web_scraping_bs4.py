import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW



internal_urls = set()
external_urls = set()

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
   
    urls = set()
    
    domain_name = urlparse(url).netloc
    try:
            soup = BeautifulSoup(requests.get(url).content,'lxml', from_encoding='utf-8')
    except AssertionError:
            print("Assertion Error")
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
           
            continue 
        href = urljoin(url, href) 
        parsed_href = urlparse(href)
       
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
        
            continue
        if href in internal_urls:
           
            continue
        if domain_name not in href:
           
            if href not in external_urls:
                print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls   

total_urls_visited = 0

def crawl(url):
    
    global total_urls_visited
    total_urls_visited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    
    if len(links)==0:
        return
    else:   
        print(total_urls_visited) 
        for link in links:
            crawl(link)

crawl('https://mppdainik.com/')
print("[+] Total Internal links:", len(internal_urls))
print("[+] Total External links:", len(external_urls))
print("[+] Total URLs:", len(external_urls) + len(internal_urls))


internal_urls=list(internal_urls)
print(len(internal_urls))

with open('website_URLS_mai_02', mode = "a", encoding = "UTF-8") as file:
    for urLs in internal_urls:
        file.write(urLs+"\n")

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
                



