import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist

route = '../assets/texto1.txt'

texto1 = open(route, encoding='utf-8')
text = texto1.read()
texto1.close()

text = nltk.word_tokenize(text)

punctuations = ".,’()[]=%"
text = [term for term in text if not (term in punctuations)]

limpio = []
save = True
for i in text:
    for word in stopwords.words('spanish'):
        if(word.lower() == i.lower()):
            save = False
        
    if( save ):
        limpio.append(i)
    
    save = True


wordFrequency = FreqDist(word for word in limpio)
print("\n",wordFrequency.most_common())