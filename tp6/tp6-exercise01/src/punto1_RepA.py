from utils import create_tfidf_representation_pdf
from utils import get_top_similar

PATH1 = './assets/ChatGPT como no caer en el prohibicionismo.pdf'
PATH2 = './assets/Simulando ChatGPT - Una experiencia de enseñanza de programación a adolescentes.pdf'
PATH3 = './assets/Encuesta de usos de ChatGPT en Argentina - resultados.pdf'
PATH4 = './assets/Acerca del auge de la IA de la mano de ChatGPT - parte 3.pdf'
PATH5 = './assets/Recursos tecnológicos en matemática - en la resolución de un problema.pdf'
PATHS=[PATH1,PATH2,PATH3,PATH4,PATH5]

#Primera representacion RepA - Texto oringinal
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_pdf(PATHS,False,False)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Texto oringinal
print("Documentos más similares para RepA (Texto original):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nPdf: {PATHS[idx]}\n")


#Primera representacion RepA - Eliminando stop-words
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_pdf(PATHS,True,False)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Eliminando stop-words
print("Documentos más similares para RepA (Eliminando stop-words):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nPdf: {PATHS[idx]}\n")

#Primera representacion RepA - Con bi-gramas
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_pdf(PATHS,True,True)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Con bi-gramas
print("Documentos más similares para RepA (Con bi-gramas):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nPdf: {PATHS[idx]}\n")
