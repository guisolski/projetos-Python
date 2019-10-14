def calculaLeds(i,leds):
  i = str(i)
  v = 0
  for a in i:
    v += leds[int(a)]

  return v


leds = [6,2,5,5,4,5,6,3,7,6] 
a = []
for i in range(int(input())):
  a.append(calculaLeds(input(),leds))

for i in a:
  print(i,"leds")
