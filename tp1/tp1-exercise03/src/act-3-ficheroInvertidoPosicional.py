from modulo import pdfToArray

PATH1 = '../assets/ChatGPT como no caer en el prohibicionismo.pdf'
PATH2 = '../assets/Simulando ChatGPT - Una experiencia de enseñanza de programación a adolescentes.pdf'
PATH3 = '../assets/Encuesta de usos de ChatGPT en Argentina - resultados.pdf'
PATH4 = '../assets/Acerca del auge de la IA de la mano de ChatGPT - parte 3.pdf'
PATH5 = '../assets/Recursos tecnológicos en matemática - en la resolución de un problema.pdf'

PDFS =[[PATH1, "D1"],[PATH2, "D2"],[PATH3, "D3"],[PATH4, "D4"],[PATH5, "D5"]]


print("\n\t ##### Inicio del programa #####")

dictionary = {}
for n in range(len(PDFS)):
    words = pdfToArray(PDFS[n][0])
    documentName = PDFS[n][1]
   
    index=0
    while index < len(words):
        if( words[index] not in dictionary):
            dictionary[words[index]] = {documentName:[]}

        if( documentName not in dictionary[words[index]]):
            dictionary[words[index]].setdefault( documentName, [])


        dictionary[words[index]][documentName].append(index)
        
        index += 1

# muestra en consola el diccionario
for word, documentAndPosition in dictionary.items():
    print("  | {:<20} |    {documentAndPosition} ".format(word,documentAndPosition=documentAndPosition))


print("\n\t ##### Fin del programa ##### \n")


"""consulta si en los documentos hay palabras adyacentes
Args: inverted_index : diccionario, representa un fichero invertido posicional
      word1_ : String que representa una palabra
      word2_ : String que representa una palabra 
      distance : Integer que representa la distancia entre terminos

returns: diccionario cuyo elemento son el nombre del documento con
        las posiciones de las palabras adjacentes 
"""
def queryAdjWords(inverted_index, word1_, word2_, distance):
    
    adjacentes = {}
    aux1 = {}
    aux2 = {}

    for document_i in inverted_index[word1_]:
        for document_j in inverted_index[word2_]:
            if(document_i == document_j):
                aux1[document_i] = inverted_index[word1_][document_i]
                aux2[document_j] = inverted_index[word2_][document_j]


    for document in aux1:
        adjacentes[document] = []

        for wordPositionOne in aux1[document]:
            for wordPositionTwo in aux2[document]:
                if(wordPositionOne == wordPositionTwo-1-distance):
                    adjacentes[document].append([wordPositionOne, wordPositionTwo])



    return adjacentes


print("inteligencia artificial (distancia 0)\n", queryAdjWords(dictionary, "inteligencia", "artificial", 0))
print("\ninteligencia generativa (distancia 1)\n", queryAdjWords(dictionary, "inteligencia", "generativa", 1))
print("\ninteligencia ChatGPT (distancia 2)\n", queryAdjWords(dictionary, "inteligencia", "ChatGPT", 2))
print("\nlimitaciones años (distancia 3)\n", queryAdjWords(dictionary, "limitaciones", "años", 3))