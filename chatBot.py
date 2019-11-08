import math
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
    return index

def maior_simi(matriz_idf):
    t = []
    for i in range(len(matriz_idf)-1):
        t.append(similaridade(matriz_idf,i))
    return index_maior_valor(t)



#resultados finais
reposta = ['Parabéns você se encaixa no perfil de morados esse são os imoveis q recomendamos para você realizar a comprar: \nCasa de Madeira - Um quarto, Duas cozinhas']
#cria casos de validação
texto = ["Shipment of gold damaged in a fire", "Delivery of silver arrived in a silver truck","Shipment of gold arrived in a truck"]
corpus = sorted(array_to_palavras(texto))
#aqui vai ser onde montamos os slots e depois o q
q = "gold silver truck"
texto.append(q)
#parte q calcula qual resposta ele chegará
matriz = matriz_idf(texto,corpus)
print(maior_simi(matriz))
