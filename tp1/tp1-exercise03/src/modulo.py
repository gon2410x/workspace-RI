import PyPDF2
import nltk
from nltk.corpus import stopwords
from tqdm import tqdm



""" funcion transforma un archivo pdf a una cadena de caracteres
Args: ruta_ : ruta relativa del pdf
Returns: String
"""
def pdfToString( ruta_ ):
    pdf_file_obj =open( ruta_, 'rb' )
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    p = 0
    text_ = ""
    while( p < len(pdf_reader.pages) ):
        page_obj = pdf_reader.pages[p]
        text_ += page_obj.extract_text() + " "
        p += 1
        
    return text_


""" funcion transforma un pdf a un array donde cada elemento del array 
    es una palabra eliminando las stopwords
Args: ruta_ : ruta del pdf dentro de la PC
Return: array[String]
"""
def pdfToArray(ruta_):

    text1 = pdfToString(ruta_)
    text = nltk.word_tokenize(text1)
    limpio_ = []

    guardar = True
    for i in tqdm(text): # genera la barra de progreso
        for word in stopwords.words('spanish'):
            if(word.lower() == i.lower() ):
                guardar = False

        if(guardar): # filtramos las stopwords
            limpio_.append(i)

        guardar = True

    return limpio_