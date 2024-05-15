import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist

# nltk.download('brown')
# nltk.download("wordnet")

corpus = brown.words('cg73')

text_cg73 = ''
for w in corpus:
    text_cg73 += w +' '

# Eliminar etiquetas HTML y XML
import re
text = re.sub(r'<[^>]+>', '', text_cg73)

# Eliminar emoticones
text = re.sub(r'(:\)|:-\)|;\)|\(:|:-\(|:-\||:O|:\'\(|:\*|:P|:D|:S|XD|:\/)', '', text)

# Tokenizar el texto
tokens = nltk.word_tokenize(text)

# Convertir a minúsculas y eliminar signos de puntuación
pattern = re.compile(r'\w+')
tokens = [token.lower() for token in tokens if pattern.match(token)]

# Obtener palabras vacías en inglés
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Eliminar palabras vacías
tokens = [token for token in tokens if token not in stop_words]

# Calcular la frecuencia de cada palabra
from collections import Counter
frecuencia_palabras = Counter(tokens)

# Obtener las 50 palabras más frecuentes
palabras_mas_frecuentes = frecuencia_palabras.most_common(100)

# Obtener las 50 stems más frecuentes
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
text_lemma_lancaster = [ st.stem(i) for i in tokens ]

stemFrequency = FreqDist(word for word in text_lemma_lancaster)
stem_mas_frecuente = stemFrequency.most_common(100)

# Obtener las 50 lemmas más frecuentes
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
lemmas = [ wordnet_lemmatizer.lemmatize(word) for word in tokens ]

lemmasFrequency = FreqDist(word for word in lemmas)
lemmas_mas_frecuente = lemmasFrequency.most_common(100)

#----------------- ACTIVIDAD 3 -------------------

COLUMNS = [ "Word", 
            "Frec_Word", 
            "Stem", 
            "Frec_Stem", 
            "Lemma", 
            "Frec_Lemma"]

rows = []

for word, frec in palabras_mas_frecuentes:
    stem = st.stem(word)
    lemma = wordnet_lemmatizer.lemmatize(word)

    x = [st_frec  for st, st_frec   in stem_mas_frecuente   if st == stem]
    y = [lem_frec for lem, lem_frec in lemmas_mas_frecuente if lem == lemma]

    if len(x) == 0: x = [0]
    if len(y) == 0: y = [0]

    row = [ word, 
            frec, 
            stem, 
            x[0],  
            lemma, 
            y[0]]

    rows.append(row)

import pandas as pd

dataFrame = pd.DataFrame(rows, columns=COLUMNS)
pd.set_option('display.max_rows', None)
print(dataFrame)

import matplotlib.pyplot as plt

titulo = ["Palabras", "Stems", "Lemmas"]

for column in range(3):
    dataFrame = dataFrame.sort_values(by=COLUMNS[column*2+1], ascending=False)
    word_and_frec = dataFrame.loc[:, [COLUMNS[column*2], COLUMNS[column*2+1]]]
    
    word_and_frec = word_and_frec.drop_duplicates()
    word_and_frec = word_and_frec[0:20]
    word_and_frec = word_and_frec.transpose().to_numpy().tolist()
    word_ = tuple(word_and_frec[0])
    frec_ = tuple(word_and_frec[1])

    plt.subplot(2, 2, column+1)
    plt.barh(word_, frec_)
    plt.ylabel('Término')
    plt.title('20 {0} más frecuentes del Texto'.format(titulo[column])) 
    plt.gca().invert_yaxis()

plt.show() 