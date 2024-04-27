import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer

# Descargar las palabras vacías en inglés si aún no las tienes
# nltk.download('stopwords')
# nltk.download('punkt')

# Definir el texto original en inglés
texto_original = """
Based on historical behaviors, sequential recommendation endeavors to predict what a user 
prefers next. The recent efforts are mainly devoted to modeling the user’s interests evolution 
process or mining multi-interests for recommendation. However, it is largely overlooked that 
the interest trend (i.e., the evolution of the main interest) and the interest diversity 
(i.e., the scattered potential interests) could complement each other for better performance. 
Specifically, the interest trend reveals the user’s basic interest and its evolution, which is 
satisfied by similarity recommendations. Nevertheless, interest diversity covers the various 
interests caused by some external environmental influence, e.g., fashion trends and 
advertisements, exploring users’ potential interests or interest diversity will facilitate 
the model for diversity and serendipity recommendation. In a way, these two factors have 
conflicting aims, we argue that they should be disentangled in modeling first and recombined 
when making personalized recommendation.
"""

# Convertir el texto a minúsculas
texto_original = texto_original.lower()

# Tokenizar el texto
tokens = word_tokenize(texto_original)

punctuations = ".,’()=%"
tokens = [term for term in tokens if not (term in punctuations)]

# Obtener las palabras vacías en inglés
stop_words = set(stopwords.words('english'))

# Eliminar las palabras vacías y realizar la tokenización
tokens_sin_stopwords = [word for word in tokens if word not in stop_words]

# Definir los objetos de los algoritmos de derivación léxica
porter = PorterStemmer()
lancaster = LancasterStemmer()

# Aplicar la derivación léxica con Porter
stem_porter = [porter.stem(token) for token in tokens_sin_stopwords]

# Aplicar la derivación léxica con Lancaster
stem_lancaster = [lancaster.stem(token) for token in tokens_sin_stopwords]

# Imprimir los resultados encolumnados
print("{:<20} {:<20} {:<20}".format("Token sin stopword", "Porter Stemming", "Lancaster Stemming"))
print("-" * 60)
for i in range(min(len(tokens_sin_stopwords), len(stem_porter), len(stem_lancaster))):
    print("{:<20} {:<20} {:<20}".format(tokens_sin_stopwords[i], stem_porter[i], stem_lancaster[i]))