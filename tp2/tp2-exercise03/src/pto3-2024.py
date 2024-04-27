import nltk
import string
from nltk.stem import SnowballStemmer

archivo = open('../assets/text1.txt', encoding='utf-8', mode='r') #abre el archivo 'texto1.txt' en modo lectura
texto1 = archivo.read()
archivo.close()
#print(texto1)

#convierte el texto a minusculas
texto1 = texto1.lower()


#tokenizacion del texto
textoTokenizado = nltk.tokenize.word_tokenize(texto1) #devuelve el texto separado en palabras (tokens)
textoTokenizado = list(filter(lambda token: token not in string.punctuation, textoTokenizado)) #elimina los signos de puntuacion


#eliminacion de los numeros
listaSinNumeros = []
for palabra in textoTokenizado:
    if palabra.isdigit():
        continue
    else:
        listaSinNumeros.append(palabra)


#eliminacion de las stopwords
stop_words = nltk.corpus.stopwords.words('spanish') #genera la lista de stopwords en espanol

listaSinStopWords = [] #lista las palabras sin stopwords
for palabra in listaSinNumeros:
    if palabra not in stop_words: #si no esta en el listado de stopwords entonces sera guardada en una lista
        listaSinStopWords.append(palabra) #Lista tokenizada sin stopWords

#print('TEXTO SIN STOPWORDS: \n',listaSinStopWords)


#Stemming con el algoritmo snowball
print('{:<18} {:<18}'.format('PALABRA', 'SNOWBALL')) #Se definen 2 columnas para mostrar los datos
print('')
for palabra in listaSinStopWords:
    conSnowball = SnowballStemmer(language='spanish').stem(palabra) #aplicacion de stemming con snowball

    print("{:<18} {:<18}".format(palabra, conSnowball))

