import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer

route = '../assets/text2.txt'

texto2 = open(route, encoding='utf-8')
text = texto2.read()
texto2.close()

text = nltk.word_tokenize(text)

punctuations = ".,’()=%"
text = [term for term in text if not (term in punctuations)]

limpio = []
save = True
for i in text:
    for word in stopwords.words('english'):
        if(word.lower() == i.lower()):
            save = False
        
    if( save ):
        limpio.append(i)
    
    save = True


st = LancasterStemmer()
text_lemma_lancaster = [ st.stem(i) for i in limpio ]

ps = PorterStemmer()
text_lemma_porter = [ ps.stem(i) for i in limpio]

print(" {0:<20} \t {1:<20} \t {2}"
    .format("- Word","- Lancaster","- Porter"))
for i in range(len(limpio)):
    print( " {0:<20} \t {1:<20} \t {2}"
    .format( limpio[i], text_lemma_lancaster[i], text_lemma_porter[i] ) )