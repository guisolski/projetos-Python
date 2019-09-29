from collections import Counter
import nltk
from nltk.corpus import stopwords


def extrac_lemma(doc):
    parsed_text = {'word': [], 'lemma': []}
    for sent in doc.sentences:
        for wrd in sent.words:
            parsed_text['word'].append(wrd.text)
            parsed_text['lemma'].append(wrd.lemma)
    return parsed_text


# le o texto e converte para lower cased
texto = str(input("Entre com um texto: ")).lower()

texto = texto.replace('\n', ' ').replace('\t', ' ').replace(',', ' ').replace('.', ' ').split(' ')
contador = Counter(texto)
print("Contando ",contador.items())


nltk.download('rslp')
stremmer = nltk.stem.RSLPStemmer()

reducida = []
for i in contador:
    reducida.append(stremmer.stem(i))
print(reducida)

nltk.download('stopwords')

stopwords = set(stopwords.words('portuguese'))

for i in reducida:
    if i in stopwords:
        reducida.remove(i)

print(reducida)
