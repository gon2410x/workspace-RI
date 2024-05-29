from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup 
import scraper

url = 'https://www.infobae.com/economia/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
htlm = urlopen(req).read()
soup = BeautifulSoup(htlm, 'lxml')
anchor = soup.find_all("a", class_="headline-link")


links = []
for link in anchor[0:10]:
    link_noticia= link.get('href')
    links.append('https://www.infobae.com/'+link_noticia)


notices = []
#Obtencion de los datos pedidos
for link in links:
    data_extract = scraper.extractData(link)  
    notices.append(data_extract)


import spacy
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from collections import Counter

for notice in notices:
    text = ''
    text += notice['title'] + " "
    text += notice['summary'] + " "
    text += notice['body'] + " "

    tokens = word_tokenize(text, language='spanish') 
    stop_words = set(stopwords.words('spanish'))
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]


    nlp = spacy.load('es_core_news_sm')
    textSpacy = ""
    for token in tokens:
        textSpacy += token + " "

    doc = nlp(textSpacy)
    LEMMA = [ L.lemma_ for L in doc]

    frecuencia_tokens = Counter(LEMMA)
    TOP_10 = frecuencia_tokens.most_common(10)

    print(TOP_10)