from urllib.request import urlopen
from bs4 import BeautifulSoup

firstTenNews = []
notices = []

html = urlopen('https://www.infobae.com/economia/')
bs = BeautifulSoup(html.read(), 'html.parser')
list__ = bs.find_all('a', class_="headline-link")
for i in range(10):
    firstTenNews.append("https://www.infobae.com/"+list__[i].get('href'))

    title = ''
    summary = ''
    body = ''
    images = []

    print(firstTenNews)
    html = urlopen(firstTenNews[i])
    bs = BeautifulSoup(html.read(), 'html.parser')
    
    list_ = bs.find_all('h1')
    for j in list_:
        title += j.string

    list_ = bs.find_all('h2', class_="article-subheadline left")
    for j in list_:
        summary += j.string

    list_ = bs.find_all('p', class_="paragraph")
    for k in list_:
        body += k.get_text() + "\n\n"

    list_ = bs.find_all('div', class_="visual__image")
    for j in list_:
        li = j.find_all('img')
        for i in li:
            images.append(i.get('src')[0:len(i.get('src'))-5])

    notice = {'title':title, 'summary':summary, 'body':body, 'imeges':images}
    notices.append(notice)


text = ''

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import spacy
nlp = spacy.load('es_core_news_sm')

for i in range(10):
    text += notices[i]['title'] + " "
    text += notices[i]['summary'] + " "
    text += notices[i]['body'] + " "


tokens = word_tokenize(text, language='spanish') 
stop_words = set(stopwords.words('spanish'))
tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]


frecuencia_tokens = Counter(tokens)
top_100 = frecuencia_tokens.most_common(100)

nlp = spacy.load('es_core_news_sm')
textSpacy = ""
for i, f in top_100:
    textSpacy += i + " "

doc = nlp(textSpacy)
lemma = [ i.lemma_ for i in doc]

print("{0:<8} {1:<8} {2:<20} {3}" .format("Ranking","Frequency", "- Word", "- Lemma"))
for i in range(100):
    print(" {0:<8} {1:<8} {2:<20} {3}" .format(i+1, top_100[i][1], top_100[i][0], lemma[i]))