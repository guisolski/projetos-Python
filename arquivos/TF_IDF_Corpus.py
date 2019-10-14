#import nltk
#from nltk.corpus import stopwords
import math


def removeStopWords(text):
    #nltk.download('stopwords')
    stopwords = ['um','a','as','do','']#set(stopwords.words('portuguese'))
    for i in text:

        for j in i:
            if j in stopwords:
                i.remove(j)
    return text

def arrayPalavras(text):
    a = []
    for i in text:
        for j in i:
            if j not in a:
                a.append(j)
    return a

def matrizFrequencia(text):
    a = arrayPalavras(text)
    m = []
    for i in text:
        f = []
        for k in a:
            f.append(i.count(k))
        m.append(f)
    return m

def buscaPalavra(p,a):
    for i in range(len(a)):
        if p == a[i]:
            return i
    return None

def buscaDocumento(n,a):
    return a[n]

def listaDocumento(t):
    dic = {}
    for i in range(len(t)):
        name = "d" + str(i+1)
        dic[name] = []
        dic[name] = i

    return dic

def calcula_Tf(matriz,arrayP,listaArquivo,palavra,nomeArquivo):
    '''Não sei é divido por 6 nessa parada'''
    return matriz[buscaDocumento(nomeArquivo,listaArquivo)][buscaPalavra(palavra,arrayP)]/6

def calcula_dft(matriz,arrayP,termo):
    a = buscaPalavra(termo,arrayP)
    s = 0
    for i in matriz:
        s += i[a]
    return s

def calcula_idf(matriz,arrayP,termo):
    b = len(matriz)
    a = calcula_dft(matriz, arrayP, termo)
    return math.log10((b/a))

def calculaTd_idf(matriz,arrayP,listaArquivo,palavra,nomeArquivo):
        return calcula_Tf(matriz,arrayP,listaArquivo,palavra,nomeArquivo) *  calcula_idf(matriz,arrayP,palavra)


texto = []
texto.append( "O carro branco está na rodovia.".replace("."," ").replace(","," ").split(" "))
texto.append( "O caminhão branco parou na garagem.".replace("."," ").replace(","," ").split(" "))
removeStopWords(texto)

dicionarioDocumento = listaDocumento(texto)
arrayP = arrayPalavras(texto)
matrizF = matrizFrequencia(texto)


for a in dicionarioDocumento:
    for i in arrayP:
        Td_idf = calculaTd_idf(matrizF,arrayP,dicionarioDocumento,i,a)
        print("Td_idf ",Td_idf," ",i," ",a)
