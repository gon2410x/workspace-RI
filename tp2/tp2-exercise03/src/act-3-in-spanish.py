import nltk
from nltk.corpus import stopwords
import spacy

route = '../assets/text1.txt'

texto1 = open(route, encoding='utf-8')
text = texto1.read()
texto1.close()

text = nltk.word_tokenize(text)

punctuations = ".,()=%"
index = 0
while(index < len(text)):
    if text[index] in punctuations:
        text.pop(index)
        index -= 1
    
    index += 1


limpio = []
save = True
for i in text:
    for word in stopwords.words('spanish'):
        if(word.lower() == i.lower()):
            save = False
        
    if( save ):
        limpio.append(i)
    
    save = True


nlp = spacy.load('es_core_news_sm')
textSpacy = ""
for i in limpio:
    textSpacy += i + " "

doc = nlp(textSpacy)
lemma = [ i.lemma_ for i in doc]

print(" {0:<20} {1}" .format("- Word", "- Lemma"))
for i in range(len(limpio)):
    print(" {0:<20} {1}" .format(limpio[i], lemma[i]))