import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse

def get_internal_links(base_url, url,domain):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    internal_links = set()
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url=""
        if href.startswith('/'):
            full_url = urljoin(base_url, href)
        elif domain in href:
            full_url=href
        if full_url and "?" not in full_url and is_new_url(full_url):
            internal_links.add(full_url)
    return internal_links


visited_urls = set()

def is_new_url(url):
    if url not in visited_urls:
        visited_urls.add(url)
        return True
    return False

def crawl_website(base_url):
    domain=urlparse(base_url).netloc
    urls_level_1 = get_internal_links(base_url, base_url,domain)
    
    urls_level_2 = set()
    for url in urls_level_1:
        urls_level_2.update(get_internal_links(base_url, url,domain))
    return urls_level_1, urls_level_2

def save_to_excel(level_1_urls, level_2_urls, file_name='urls.xlsx'):
    data = {
        'Nivel 1': list(level_1_urls),
        'Nivel 2': list(level_2_urls)
    }
    
    df_level_1 = pd.DataFrame(data['Nivel 1'], columns=['URLs Nivel 1'])
    df_level_2 = pd.DataFrame(data['Nivel 2'], columns=['URLs Nivel 2'])
    
    with pd.ExcelWriter(file_name) as writer:
        df_level_1.to_excel(writer, sheet_name='Nivel 1', index=False)
        df_level_2.to_excel(writer, sheet_name='Nivel 2', index=False)

if __name__ == "__main__":
    base_url = 'https://eltribunodejujuy.com/'
    level_1_urls, level_2_urls = crawl_website(base_url)
    save_to_excel(level_1_urls, level_2_urls)