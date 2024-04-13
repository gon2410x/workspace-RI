from modulo import pdfToArray

PATH1 = '../assets/ChatGPT como no caer en el prohibicionismo.pdf'
PATH2 = '../assets/Simulando ChatGPT - Una experiencia de enseñanza de programación a adolescentes.pdf'
PATH3 = '../assets/Encuesta de usos de ChatGPT en Argentina - resultados.pdf'
PATH4 = '../assets/Acerca del auge de la IA de la mano de ChatGPT - parte 3.pdf'
PATH5 = '../assets/Recursos tecnológicos en matemática - en la resolución de un problema.pdf'

PDFS = [[PATH1, "D1"],[PATH2, "D2"],[PATH4, "D4"],[PATH3, "D3"],[PATH5, "D5"]]

print("\n\t ##### Inicio del programa #####")

dictionary = {}
for n in range( len(PDFS) ):
    words = pdfToArray( PDFS[n][0] )
    documentName = PDFS[n][1]
    
    index = 0
    while index < len(words):
        if( words[index] not in dictionary):
            dictionary[ words[index] ] = {documentName:0}

        if( documentName not in dictionary[words[index]]):
            dictionary[ words[index] ].setdefault( documentName, 0)


        dictionary[words[index]][documentName] += 1
        index += 1


for word, documentAndFrequency in dictionary.items():
    print("  | {:<20} |    {documentAndFrequency} ".format(word,documentAndFrequency=documentAndFrequency))


print("\n\t ##### Fin del programa ##### \n")

print(len(dictionary))
