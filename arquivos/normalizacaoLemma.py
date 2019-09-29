from collections import Counter
import stanfordnlp
import nltk
from nltk import tokenize
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


stanfordnlp.download('pt')
nlp = stanfordnlp.Pipeline()

reducida = ""
for i in contador:
     reducida += " " + i



doc = nlp(reducida)
doc = extrac_lemma(doc)

print(doc)


nltk.download('stopwords')

stopwords = set(stopwords.words('portuguese'))
t = doc['lemma']

for i in t:
     if i in stopwords:
         t.remove(i)

print(t)
