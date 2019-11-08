import math
def arrayPalavras(text):
    a = []
    for i in text:
        for j in i.split(" "):
            if j not in a:
                a.append(j)
    return a
def df(documents,word):
  s = 0
  for i in documents:
      if word in i:
        s += 1
  return s
def idf(documents,word):
  #-2 porque tem o corpus incluido
  t = len(documents)
  d = df(documents,word)
  print(t)
  print(d)
  return math.log10((t/d))

def matriz_idf(documents,list_word):
  m = []
  for i in range(len(documents)-1):
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
        s += (matriz_idf[i][j] * matriz_idf[len(matriz_idf)-1][j])
    return s

texto = ["Shipment of gold damaged in a fire", "Delivery of silver arrived in a silver truck","Shipment of gold arrived in a truck"]

corpus = sorted(arrayPalavras(texto))
#q = "gold silver truck"
#texto.append(q)
print(idf(texto,"truck"))
