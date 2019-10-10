a = ["1111","11"]
soma = ""

for i in range(len(a[0]) if len(a[0]) > len(a[1]) else len(a[1])):
        if i < len(a[0]) and i < len(a[1]):
            soma += str(int(a[0][i]) + int(a[1][i]))
        elif i > len(a[0])-1:
            soma += str(int(a[1][i]))
        elif i > len(a[1])-1:
            soma += str(int(a[0][i]))

print(soma)
