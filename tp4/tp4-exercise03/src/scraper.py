from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def extractData(url_nota):

    notice = {}

    # Read link
    req = Request(url_nota, headers={ 'User-Agent': 'Mozilla/5.0'})
    htlm = urlopen(req).read()
    soup = BeautifulSoup (htlm, 'lxml')

    # Extract title
    title = soup.find('h1').text
    notice['title'] = title

    # Extract summary
    summary = soup.find('h2', class_="article-subheadline left").string
    notice['summary'] = summary

    # Extract paragraph 
    body = ''
    p = soup.find_all('p', class_="paragraph")
    for paragraph in p:
        body += paragraph.get_text() + "\n\n"
    notice['body']= body

    # Extract image
    images = []
    divs = soup.find_all('div', class_="visual__image")
    for div in divs:
        imgs = div.find_all('img')
        for sourceImg in imgs:
            images.append(sourceImg.get('src')[0:len(sourceImg.get('src'))-5])
    notice['image'] = images

    return notice