from utils import create_tfidf_representation_txt
from utils import get_top_similar

PATH1 = './assets/news-1.txt'
PATH2 = './assets/news-2.txt'
PATH3 = './assets/news-3.txt'
PATH4 = './assets/news-4.txt'
PATH5 = './assets/news-5.txt'
PATH6 = './assets/news-6.txt'
PATH7 = './assets/news-7.txt'
PATH8 = './assets/news-8.txt'
PATH9 = './assets/news-9.txt'
PATH10 = './assets/news-10.txt'
PATHS=[PATH1,PATH2,PATH3,PATH4,PATH5,PATH6,PATH7,PATH8,PATH9,PATH10]

#Primera representacion RepA - Texto oringinal
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_txt(PATHS,False,False)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Texto oringinal
print("Documentos más similares para RepB (Texto original):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nTXT: {PATHS[idx]}\n")


#Primera representacion RepA - Eliminando stop-words
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_txt(PATHS,True,False)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Eliminando stop-words
print("Documentos más similares para RepB (Eliminando stop-words):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nTXT: {PATHS[idx]}\n")

#Primera representacion RepA - Con bi-gramas
tfidf_matrix_repA, preprocessed_docs_repA = create_tfidf_representation_txt(PATHS,True,True)
top_indices_repA, scores_repA = get_top_similar(tfidf_matrix_repA)

# Mostrar resultados para RepA - Con bi-gramas
print("Documentos más similares para RepB (Con bi-gramas):")
for idx, score in zip(top_indices_repA, scores_repA):
    print(f"Score: {score}\nTXT: {PATHS[idx]}\n")
