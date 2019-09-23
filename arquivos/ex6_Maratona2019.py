#link question http://maratona.ime.usp.br/primfase19/provas/competicao/maratona.pdf
def maior(X, L):
  m = 0
  for i in range(len(X)):
    if X[i] not in L and X[i]> m:
      m = i
  return m
def converte(X):
  k = []
  for i in X:
      k.append(int(i))
  return k



a = converte(input().split(" "))
b = converte(input().split(" ")) 
#b = [1 ,1 ,2, 2, 3, 3, 4 ,4, 5]
L= []
cont = 0
for i in range(a[1]):
    q = maior(b,L)
    L.append(b[q])
    cont += 1
    while b[q-1] != 1:
        cont += 1
        q = b[q-1]


print(cont)
