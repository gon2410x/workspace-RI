import nltk
from nltk.util import ngrams

route = '../assets/texto1-primer-parafo.txt'
corpus = open(route, encoding="utf-8")
text = corpus.read()
corpus.close()

text = nltk.word_tokenize(text)

punctuations = ".,()=%"
text = [term for term in text if not (term in punctuations)]

twoGrams = ngrams(text,2)
print("\n\t2-grams\n\n", [" ".join(term) for term in twoGrams])

threeGrams = ngrams(text,3)
print("\n\t3-grams\n\n", [" ".join(term) for term in threeGrams])