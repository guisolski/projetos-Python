alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def remove(t):
  k = []
  for i in t:
    if i in alfabeto:
      k.append(i)
  
  return k
def cont(t):
  t = remove(t)
  c = {}
  teta = []
  for i in t:
    if i not in teta:
      c[i] = t.count(i)
    teta.append(i)
  return c

def maior(t):
  t = cont(t)
  maior = 0
  for i in t:
    if t[i] > maior:
      maior = t[i]
  return [k for k,v in t.items() if float(v) == maior]

def montaString(t):
  t = maior(t)
  print(t)
  k = ""
  for i in t:
    k += i
  return k


tea = []
#tea.append(input())
for i in range(int(input())):
    
    tea.append(montaString(input().lower()))
for i in tea:
  print(i)
