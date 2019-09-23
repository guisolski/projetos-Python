def maior(X):
  m = 0
  for i in X:
    if len(i) > m:
      m = len(i)
  return m
a = int(input())
c = []
while a !=0:  
  b = []
  for i in range(a):
    b.append(input())
  
  c.append(b)
  a = int(input())
print()
for i in c:
  k = str('{:>'+str(maior(i))+'}')
  for t in i:
      print(k.format(t.strip()))
  print()
