import math
from collections import Counter
import nltk
from nltk.corpus import stopwords
import sys


def extrac_lemma(doc):
    parsed_text = {'word': [], 'lemma': []}
    for sent in doc.sentences:
        for wrd in sent.words:
            parsed_text['word'].append(wrd.text)
            parsed_text['lemma'].append(wrd.lemma)
    return parsed_text


def normalizacao(texto, stopwords):
    # le o texto e converte para lower cased
    texto = texto.lower().replace('\n', ' ').replace('\t', ' ').replace(',', ' ').replace('.', ' ').split(' ')
    contador = Counter(texto)
    # print("Contando ",contador.items())

    nltk.download('rslp')
    stremmer = nltk.stem.RSLPStemmer()

    reducida = []
    for i in contador:
        reducida.append(stremmer.stem(i))
    for i in reducida:
        if i in stopwords:
            reducida.remove(i)
    return " ".join(str(x) for x in reducida)


def array_normalize(arr, stopwords):
    return [normalizacao(str(i), stopwords) for i in arr]
    #return [i for i in arr]


def arraysWords_to_arrayWord(text):
    a = []
    for i in text:
        for j in i.split(" "):
            if j not in a:
                a.append(j)
    return a


def df(documents, word):
    s = 0
    # -1 porque tem o q incluido
    for i in range(len(documents) - 1):
        if word in documents[i]:
            s += 1
    return s


def idf(documents, word):
    # -1 porque tem o q incluido
    t = len(documents) - 1
    d = df(documents, word)
    return math.log10((t / d))


def matriz_idf(documents, list_word):
    m = []
    # não prisa do -1 pq agora estamos montando a matriz
    for i in range(len(documents)):
        t = []
        for j in list_word:
            if j in documents[i]:
                t.append(idf(documents, j))
            else:
                t.append(0)
        m.append(t)
    return m


def similaridade(matriz_idf, i):
    s = 0
    for j in range(len(matriz_idf[0])):
        if matriz_idf[i][j] != 0 and matriz_idf[len(matriz_idf) - 1][j] != 0:
            s += matriz_idf[i][j] * matriz_idf[len(matriz_idf) - 1][j]
    return s


def index_maior_valor(t):
    m = t[0]
    index = 0
    for i in range(len(t)):
        if t[i] > m:
            index = i
            m = t[i]
    return index if t[index] != 0 else None


def maior_simi(matriz_idf):
    t = []
    for i in range(len(matriz_idf) - 1):
        t.append(similaridade(matriz_idf, i))
    return index_maior_valor(t)


def arrays_to_unicArray_normalized(stopwords, *args):
    return [normalizacao(j, stopwords) for i in args for j in i]
    #return [j for i in args for j in i]


def resposta(*args):
    tamanho = 0
    for i in range(1, len(args)):
        tamanho += len(args[i])
        if args[0] < tamanho: return i - 1 if i >= 1 else 0
    return None


# define stopwords
# nltk.download('stopwords')
stopwords = ['a', 'e']  # set(stopwords.words('portuguese'))

# resultados finais
reposta = [
    "Parabéns você se encaixa no perfil de morador esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Bronze - Um quarto,",
    "Parabéns você se encaixa no perfil de alugador esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Prata - Um quarto,",
    "Parabéns você se encaixa no perfil de investidor esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Gold - Um quarto,",
    "Parabéns você se encaixa no perfil de um fundo imobiliario esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Platina - Um quarto,",
    "Responda a serio as perguntas"]

# cria casos de validação
morar = ["Moradia não não", "Moradia não sim", "Para morar não não", "Para morar não sim",
         "Eu gostaria de morar na casa não não",
         "Eu gostaria de morar na casa não sim", "Morar não não", "Morar não sim",
         "morar é o meu intuido porem como eu vou morar se tem alguem morando na casa tá loko oque e pendencia juridica","não não não"]
alugar = ["Para alugar não não", "Para alugar não sim", "Aluguel não não", "Aluguel não sim",
          "Eu gostaria de alugar a casa não não", "Eu gostaria de alugar a casa não sim", "Alugar não não",
          "Alugar não sim"]
investir = ["Investimento sim não", "Investimento não não", "Investir sim não", "Investir não não",
            "Para investir sim não",
            "Para investir não não", "Eu gostaria de investir no imovel sim não",
            "Eu gostaria de investir no imovel não não",
            "eu gostaria de ampliar o numero de imoveis que eu possuo",
            "eu gostaria de ampliar o numero de imoveis que eu possuo tanto faz não"]
fundo_imobi = ["Fundo imobiliario sim sim", "Fundo imbiliario sim não",
               "Eu gostaria de acionar ao meu portifolio de imoveis sim sim",
               "Eu gostaria de acionar ao meu portifolio de imoveis sim não",
               "Eu gostaria de acionar ao meu portifolio de imoveis tanto faz sim",
               "acrescentar na minha carteira de imoveis tanto faz tanto faz tanto faz",
               "acrescentar na minha carteira de imoveis tanto faz sim não",
               "acrescentar na minha carteira de imoveis sim sim", "acrescentar na minha carteira de imoveis"]
sem_sentido = ["porra", "foda-se", "foda-se", "foda-se foda-se foda-se", "sei la","sei-la","cuscuz","tete"]
# junta tos em um unico array, já normalizando, para depois poder criar o corpu
validacoes = arrays_to_unicArray_normalized(stopwords, morar, alugar, investir, fundo_imobi, sem_sentido)
corpus = arraysWords_to_arrayWord(validacoes)
# perguntas
perguntas = ["Qual o seu intuito com compra/aquicição do imovel?",
             "A compra de um imovel com a possibilidade de ainda ter um morador dentro lhe interessa?",
             "A compra de um imovel com a possibilidade de alguma pendência juridica lhe interessa?",
             "Em um futuro proximo o imovel tem lhe trazer algum tipo de retorno financieiro?"]

# aqui vai ser onde montamos os slots e depois o q
slots = []

for i in perguntas:
    print(i)
    print("Resposta: ", end=" ")
    resposta_slot = ""
    while(resposta_slot == ""):
        resposta_slot = str(input()).strip()
        if(resposta_slot == ""): print("Responda a pergunta\nRespota:",end=" ")
    slots.append(resposta_slot)

q = arraysWords_to_arrayWord(array_normalize(slots, stopwords))

if (q == None or q[0] == ""):
    print("invalido")
    sys.exit()
validacoes.append(q)

# parte q calcula qual resposta ele chegará
matriz = matriz_idf(validacoes, corpus)
index = maior_simi(matriz)
if index == None:
    print("invalido")
    sys.exit()

r_index = resposta(index, morar, alugar, investir, fundo_imobi, sem_sentido)
print(reposta[r_index])
