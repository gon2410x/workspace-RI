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
palabras_mas_frecuentes = frecuencia_palabras.most_common(50)
print(palabras_mas_frecuentes)

# Obtener las 50 stems más frecuentes
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
text_lemma_lancaster = [ st.stem(i) for i in tokens ]

stemFrequency = FreqDist(word for word in text_lemma_lancaster)
print("\n",stemFrequency.most_common(50))

# Obtener las 50 lemmas más frecuentes
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
lemmas = [ wordnet_lemmatizer.lemmatize(word) for word in tokens ]

lemmasFrequency = FreqDist(word for word in lemmas)
print("\n",lemmasFrequency.most_common(50))

# lemmatizacion indicando PoS
lemmasSoP = [ wordnet_lemmatizer.lemmatize(word, pos="v") for word in tokens ]

# representación tabular de los primeros 30 tokens
most_frequent_words = FreqDist(word for word in tokens)
most_frequent_words = most_frequent_words.most_common(30)

print(" {0:<20} \t {1:<20}  \t {2:<20} \t {3}"
    .format("- Word","- Lancaster","- Lemma", "Lemma SoP"))
for word, frecuency in most_frequent_words :
    print( " {0:<20} \t {1:<20} \t {2:<20} \t {3}"
    .format( word, 
             st.stem(word), 
             wordnet_lemmatizer.lemmatize(word), 
             wordnet_lemmatizer.lemmatize(word, pos="v") ) )