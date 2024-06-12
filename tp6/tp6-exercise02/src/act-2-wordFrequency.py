import nltk
from nltk.corpus import inaugural
# nltk.download('inaugural')

obamaDiscurse = inaugural.sents('2009-Obama.txt')
discourse = ''
for sent in obamaDiscurse:
    for word in sent:
        discourse += word + ' '


import re
from nltk import word_tokenize, sent_tokenize
  
#EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
text = re.sub('[^a-zA-Z]', ' ', discourse )  
text = re.sub(r'\s+', ' ', text)  
stopwords = nltk.corpus.stopwords.words('english')
 
word_frequencies = {}  
for word in nltk.word_tokenize(text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
 

maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
 
#CALCULA LAS FRASES QUE MÁS SE REPITEN
sentences = nltk.sent_tokenize(discourse)  
sentence_scores = {}  
for sent in sentences:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
 
#REALIZA EL RESUMEN CON LAS MEJORES FRASES
import heapq  
summary = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary)  
print("\n * Summary *\n\n", summary)  