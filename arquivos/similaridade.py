def unicos(X):
    B = []
    for i in range(len(X)):
        if(i<= len(X)-2):
          aux = str(X[i])+str(X[i+1])
          if(aux in B):
              B.remove(aux)
          else:
              B.append(aux)
    return B

def compart(X,Y):
    intercalada = []
    for a,b in zip(X, Y):
        intercalada.append(a)
    return intercalada
    
def simi(X,Y):
  x = unicos(X)
  y = unicos(Y)
  co = len(compart(x,y))
  A = len(x)
  B = len(y)
  C = co
  return (2*C)/(A+B)

def maior(X,lista):
    m = 0
    t = 0
    for i in range(len(X)):
        if X[i] > m:
          m = X[i]
          t = i
    return [m,lista[t],t]

def listaSimi(lista,P):
    B = []
    for i in lista:
        B.append(simi(i,P))
    return B

def ordena(lista,P):
    B = []
    L = listaSimi(lista,P)
    while len(L) >= 1:
        m = maior(L,lista)        
        B.append([m[0],m[1]])
        lista.remove(m[1])
        L.pop(m[2])
    return B
    
lexico  = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 'ananás', 'maça', 'mamão',
'manga', 'melancia', 'melão', 'mexerica', 'morango']

o = ordena(lexico,'abacate')
for i in o:
  print(i)
