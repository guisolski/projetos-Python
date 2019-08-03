m = int(input("entre com valor de m: "))
a = int(input("entre com valor de a: "))
c = int(input("entre com valor de c: "))
x = int(input("entre com valor de x: "))




if(a >= 2 and c>=0 and x>=0):
        for i in range(100):
            x = float(((a*x)+c)%m)
            print(x)
else:
    print("entre com a maior q 2")
