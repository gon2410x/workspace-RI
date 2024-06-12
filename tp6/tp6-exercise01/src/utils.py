from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk import ngrams
import PyPDF2
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))


#Funcion para convertir de archivo pdf a string
def pdfToString( ruta_):
    pdf_file_obj =open( ruta_, 'rb' )
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    p = 0
    text_ = ""
    while( p < len(pdf_reader.pages) ):
        page_obj = pdf_reader.pages[p]
        text_ += page_obj.extract_text() + " "
        p += 1
    return text_
#Funcion para convertir de archivo txt a string
def txtToString( ruta_):
    with open(ruta_, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Función para preprocesar texto, remover stopwords o usar bigramas
def preprocess_text(text, remove_stopwords, use_bigrams):
    # Tokenización
    tokens = nltk.word_tokenize(text.lower())
    # Eliminación de stop-words
    if remove_stopwords:
        tokens = [word for word in tokens if word not in stop_words]
    # Eliminación de puntuación
    tokens = [word for word in tokens if word.isalnum()]
    # Creación de bi-gramas si es necesario
    if use_bigrams:
        tokens = [' '.join(gram) for gram in ngrams(tokens, 2)]
    return ' '.join(tokens)

# Preprocesar documentos pdf para poder obtener la matriz
def preprocess_documents_pdf(docs, remove_stopwords, use_bigrams):
    return [preprocess_text(pdfToString(doc), remove_stopwords, use_bigrams) for doc in docs]

# Preprocesar documentos txt para poder obtener la matriz
def preprocess_documents_txt(docs, remove_stopwords, use_bigrams):
    return [preprocess_text(txtToString(doc), remove_stopwords, use_bigrams) for doc in docs]

# Crear y mostrar representación TF-IDF para pdf
def create_tfidf_representation_pdf(docs, remove_stopwords, use_bigrams):
    preprocessed_docs = preprocess_documents_pdf(docs, remove_stopwords, use_bigrams)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)
    return tfidf_matrix, preprocessed_docs

# Crear y mostrar representación TF-IDF para txt
def create_tfidf_representation_txt(docs, remove_stopwords, use_bigrams):
    preprocessed_docs = preprocess_documents_txt(docs, remove_stopwords, use_bigrams)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)
    return tfidf_matrix, preprocessed_docs

# Calcular similitud y obtener top 3
def get_top_similar(tfidf_matrix, query_index=0, top_n=3):
    query_vector = tfidf_matrix[query_index]
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    #Mostrar similitudes de todos los pdf
    print("---------- Scores ---------")
    print(cosine_similarities)
    print("---------------------------")
    # Obtener índices de los documentos más similares
    similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]
    return similar_indices, cosine_similarities[similar_indices]
