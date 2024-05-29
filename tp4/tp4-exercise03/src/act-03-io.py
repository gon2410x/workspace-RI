from urllib.request import urlopen
from bs4 import BeautifulSoup

firstTenNews = []
notices = []

html = urlopen('https://www.infobae.com/economia/')
bs = BeautifulSoup(html.read(), 'html.parser')
a = bs.find_all('a', class_="headline-link")
for i in range(10):
    firstTenNews.append("https://www.infobae.com/"+a[i].get('href'))

    title = ''
    summary = ''
    body = ''
    images = []

    print(firstTenNews)
    html = urlopen(firstTenNews[i])
    bs = BeautifulSoup(html.read(), 'html.parser')
    
    h1 = bs.find_all('h1')
    for sentence in h1:
        title += sentence.string

    h2 = bs.find_all('h2', class_="article-subheadline left")
    for sentence in h2:
        summary += sentence.string

    p = bs.find_all('p', class_="paragraph")
    for paragraph in p:
        body += paragraph.get_text() + "\n\n"

    divs = bs.find_all('div', class_="visual__image")
    for div in divs:
        imgs = div.find_all('img')
        for sourceImg in imgs:
            images.append(sourceImg.get('src')[0:len(sourceImg.get('src'))-5])

    notice = {'title':title, 'summary':summary, 'body':body, 'imeges':images}
    notices.append(notice)



import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import spacy
nlp = spacy.load('es_core_news_sm')

for i in range(10):
    text = ''
    text += notices[i]['title'] + " "
    text += notices[i]['summary'] + " "
    text += notices[i]['body'] + " "

    tokens = word_tokenize(text, language='spanish') 
    stop_words = set(stopwords.words('spanish'))
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]

    nlp = spacy.load('es_core_news_sm')
    textSpacy = ""
    for token in tokens:
        textSpacy += token + " "

    doc = nlp(textSpacy)
    lemma = [ l.lemma_ for l in doc]

    frecuencia_tokens = Counter(lemma)
    top_10 = frecuencia_tokens.most_common(10)

    notices[i]['top10'] = top_10
    print(notices[i]['top10'])
