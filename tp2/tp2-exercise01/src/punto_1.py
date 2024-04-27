import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Descargar los recursos necesarios de NLTK
#nltk.download('punkt')
#nltk.download('stopwords')

# Definir el texto
texto1 = """
Los sistemas recomendadores son herramientas enfocadas a ayudar a los usuarios a obtener
aquella información que mejor se corresponda con sus intereses y preferencias. Mientras que
un buscador habitual se centra en encontrar aquello que el usuario solicita, un sistema
recomendador ayuda al usuario a tomar una decisión, que puede ser la compra de un
producto en un portal de comercio electrónico, la lectura de un libro, la revisión de un
artículo científico, el acceso a una página web en específico, o el estudio de determinado
recurso educativo en una plataforma virtual de aprendizaje.
La clasificación más popular de los sistemas recomendadores está asociada al algoritmo que
emplean para realizar la tarea de minería correspondiente y divide a los métodos de
recomendación en métodos de filtrado basado en el contenido, métodos de filtrado
colaborativo, métodos de filtrado demográfico y métodos híbridos [1-4]. En adición, la
literatura ha desarrollado tanto sistemas recomendadores para la sugerencia de ítems para
usuarios individuales, como enfocados en grupos de usuarios []. Así, los sistemas
recomendadores enfocados en grupos de usuarios se centran en la sugerencia de
determinados tipos de ítems que tienden a ser consumidos en grupos y no por usuarios
individuales, tales como programas de televisión y paquetes turísticos [].
De manera general, los dominios iniciales de aplicación de los sistemas recomendadores han
sido el e-commerce[]y el e-learning[, ], aunque en los últimos tiempos estos sistemas están
siendo aplicados a escenarios cada vez más diversos []. Así, son relevantes las aplicaciones
de los sistemas recomendadores en escenarios de e-health[] y de e-tourism[], como dos
contextos relevantes de particular importancia.
Específicamente, resulta importante en los últimos años el desarrollo de sistemas
recomendadores en el dominio del turismo[]. En este dominio existe mucha información en
línea disponible y por tanto los sistemas recomendadores juegan un papel muy importante
con vistas a ayudar a los usuarios en la toma de decisiones sobre qué paquete turístico
comprar, qué instalación hotelera visitar, o qué recorrido turístico elegir, entre otras
decisiones similares a tomar con vistas a lograr la satisfacción final del cliente [].
"""

# Tokenizar el texto y eliminar las stop words
tokens = word_tokenize(texto1, language='spanish')
stop_words = set(stopwords.words('spanish'))
tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]

# Contar la frecuencia de cada término
frecuencia_tokens = Counter(tokens)

# Mostrar los términos más frecuentes
print("Términos más frecuentes:")
for palabra, frecuencia in frecuencia_tokens.most_common():
    print(f"{palabra}: {frecuencia}")

# Mostrar un gráfico con los 20 términos más frecuentes
top_20 = frecuencia_tokens.most_common(20)
palabras, frecuencias = zip(*top_20)
plt.figure(figsize=(10, 6))
plt.barh(palabras, frecuencias)
plt.xlabel('Frecuencia')
plt.ylabel('Término')
plt.title('20 términos más frecuentes en Texto1')
plt.gca().invert_yaxis()
plt.show()