import  math
def somatoria(listaV, valor):
    soma = None
    for i in listaV:
        if i <= valor:
            if soma == None:
                soma = 0
            soma += i
        else:
            return soma

'''Exercicio 1'''

'''Letra A'''
print("Letra A exercicio 1: ")

def a1(n):
    listV = []
    valor = 2
    while valor <= 1000:
        listV.append(valor)
        valor += 4

    return somatoria(listV,(4*n-2)) == 2*n**2

def buscaBase():
    for i in range(1000):
        if(a1(i)):
            return i
    return None
def prova():
    base = buscaBase()
    if base!= None:
        print("Base: ", base)
        for k in range(1000):
             if (2*k**2+4*k+2) == (2*(k+1)**2):
                return True
    else:
        return False
print(prova())

'''Letra B'''

print("Letra B exercicio 2: ")

def b1(n):
    listV = []
    valor = 1
    while valor <= 1000:
        listV.append(valor)
        valor += 4

    return somatoria(listV,(4*n-3)) == n*(2*n-1)

def buscaBase():
    for i in range(1000):
        if(b1(i)):
            return i
    return None
def prova():
    base = buscaBase()
    if base!= None:
        print("Base: ", base)
        for k in range(1000):
             if (k*(2*k-1)+4*(k+1)-3) == (k+1)*(2*(k+1)-1):
                return True
    else:
        return False
print(prova())



'''Letra C'''

print("Letra C exercicio 1: ")

def c1(n):
    listV = []
    valor = 4
    while valor <= 1000:
        listV.append(valor)
        valor += 6

    return somatoria(listV,(6*n-2)) == n*(3*n+1)

def buscaBase():
    for i in range(1000):
        if(c1(i)):
            return i
    return None
def prova():
    base = buscaBase()
    if base!= None:
        print("Base: ", base)
        for k in range(1000):
             if (k*(3*k+1)+6*(k+1)-2) == (k+1)*(3*(k+1)+1):
                return True
    else:
        return False
print(prova())


'''Letra D'''

print("Letra D exercicio 1: ")

def d1(n):
    if n >= 4:
        return 2**n < math.factorial(n)
    return False

def buscaBase():
    for i in range(4,1000):
        if(d1(i)):
            return i
    return None
def prova():
    base = buscaBase()
    if base!= None:
        print("Base: ", base)
        for k in range(4,1000):
             if (math.factorial(k)+(2**(k+1))) < math.factorial(k+1):
                return True
        return False
    else:
        return False

print(prova())

'''Letra E'''

print("Letra E exercicio 1: ")

def e1(n):
    listV = []
    for valor in range(1,1000):
        listV.append(valor)
    return somatoria(listV,n) < n**2

def buscaBase():
    for i in range(1,1000):
        if(e1(i)):
            return i
    return None
def prova():
    base = buscaBase()
    if base != None:
        print("Base: ", base)
        for k in range(1000):
             if (k**2)+(k+1) == (k+1)**2:
                return True
    else:
        return False
print(prova())
