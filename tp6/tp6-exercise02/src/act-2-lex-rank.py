import nltk
from nltk.corpus import inaugural

obamaDiscurse = inaugural.sents('2009-Obama.txt')

discurse = []
for sent in obamaDiscurse:
    text = ''
    for word in sent:
        text += word + ' '
    
    discurse.append(text)

from lexrank import STOPWORDS, LexRank
from path import Path

documents = []
documents_dir = Path('bbc/politics')


for file_path in documents_dir.files('*.txt'):
    with file_path.open(mode='rt', encoding='utf-8') as fp:
        documents.append(fp.readlines())


lxr = LexRank(documents, stopwords=STOPWORDS['en'])

# get summary with classical LexRank algorithm
summary = lxr.get_summary(discurse, summary_size=7, threshold=.1)
summary = ' '.join(summary)  
print("\n * Summary *\n\n", summary)