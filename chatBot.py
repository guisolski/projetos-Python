import math
import functools

def array_to_palavras(text):
    a = []
    for i in text:
        for j in i.split(" "):
            if j not in a:
                a.append(j)
    return a
def df(documents,word):
  s = 0
  # -1 porque tem o q incluido
  for i in range(len(documents)-1):
      if word in documents[i]:
        s += 1
  return s
def idf(documents,word):
  #-1 porque tem o q incluido
  t = len(documents)-1
  d = df(documents,word)
  return math.log10((t/d))

def matriz_idf(documents,list_word):
  m = []
  # não prisa do -1 pq agora estamos montando a matriz
  for i in range(len(documents)):
    t = []
    for j in list_word:
      if j in documents[i]:
        t.append(idf(documents,j))
      else:
        t.append(0)
    m.append(t)
  return m
def similaridade(matriz_idf,i):
    s = 0
    for j in range(len(matriz_idf[0])):
        if matriz_idf[i][j] != 0 and matriz_idf[len(matriz_idf)-1][j] != 0:
                s += matriz_idf[i][j]*matriz_idf[len(matriz_idf)-1][j]
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
    for i in range(len(matriz_idf)-1):
        t.append(similaridade(matriz_idf,i))
    return index_maior_valor(t)

def arrays_to_unicArray(*args):
  return [j for i in args for j in i]

def resposta(*args):
    for i in range(len(args)):
        print(args)
        #tamanho = functools.reduce(lambda a,b : len(a)+len(b),args[0:i+1])
        #print(tamanho)
        #if index < tamanho: return i
    return None


#resultados finais
reposta = ["Parabéns você se encaixa no perfil de morados esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Madeira - Um quarto,",
           "Parabéns você se encaixa no perfil de alugador esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Madeira - Um quarto,",
           "Parabéns você se encaixa no perfil de investidor esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Madeira - Um quarto,",
           "Parabéns você se encaixa no perfil de um fundo imobiliario esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Madeira - Um quarto,"]
#cria casos de validação
morar = ["Eu gostaria de morar na casa não não", "Eu gostaria de morar na casa não sim", "Morar não não","Morar não sim" ]
alugar = ["Eu gostaria de alugar a casa não não","Alugar não não","Alugar não sim"]
investir = ["Eu gostaria de investir no imovel sim não","Eu gostaria de investir no imovel não não"]
fundo_imobi = ["Eu gostaria de acionar ao meu portifolio de imoveis sim sim","Eu gostaria de acionar ao meu portifolio de imoveis sim não","Eu gostaria de acionar ao meu portifolio de imoveis tanto faz sim"]

validacoes = arrays_to_unicArray(morar,alugar,investir,fundo_imobi)
corpus = array_to_palavras(validacoes)
#perguntas
perguntas = ["Qual o seu intuito com compra/aquicição do imovel?",
            "A compra de um imovel com a possibilidade de ainda ter um morador dentro lhe interessa?",
             "A compra de um imovel com a possibilidade de alguma pendência juridica lhe interessa?"]
#aqui vai ser onde montamos os slots e depois o q
slot = ["Investir imovel","não","não"]
'''
for i in perguntas:
    print(i)
    print("Resposta: ",end=" ")
    slot.append(str(input()))
'''

q = array_to_palavras(slot)
validacoes.append(q)
#parte q calcula qual resposta ele chegará
matriz = matriz_idf(validacoes,corpus)
index = maior_simi(matriz)
print(index)
r_index = resposta(index, morar,alugar,investir,fundo_imobi)
#print(reposta[r_index])
