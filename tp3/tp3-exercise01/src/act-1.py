import nltk
from nltk.corpus import brown
# nltk.download('brown')

corpus = brown.sents('cg73')
print(corpus)


# Mostrar las primeras 10 oraciones
print("Las primeras 10 oraciones:")
for i, sentence in enumerate(corpus[:10]):
    print(f"{i+1}. {sentence}")