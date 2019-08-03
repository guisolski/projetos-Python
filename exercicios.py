''' Exercicios '''

''' "O produto de dois pares é par". '''

def ex1 (x,y):
    if x%2 == 0 and y%2 ==0:
         if (x*y)%2 ==0:
             return True
    return False

''' "O produto de dois números ímpares é ímpar". '''
def ex2 (x,y):
    if x%2 != 0 and y%2 !=0:
         if (x*y)%2 !=0:
             return True
    return False

''' "A soma de dois ímpares é par".  '''
def ex3 (x,y):
    if x%2 != 0 and y%2 !=0:
         if (x+y)%2 ==0:
             return True
    return False

''' Provar por contradição.
 "Se um número somado a ele próprio resulta no próprio número,então o número é 0 (zero)".  '''
'''tese '''
def ex4T (x):
    if x+x == x:
        if x==0:
            return True
    return False
'''Prova'''
def ex4Prova(x):
    if x+x == x:
        if x != 0:
            return False
    return  True #a contratição estava errada, ou seja x é 0, portanto a tese é verdadeira, por isso retorno True


'''"Se um inteiro é divisível por 6, então duas vezes o inteiro é divisível por 4". '''
'''Tese'''
def ex5T(x):
    if x%6==0:
        if (x*2)%4==0:
            return True
    return False
'''Prova por contratição'''
def ex5Prova(x):
    if x%6==0:
        if (x*2)%4 !=0:
            return False
    return True#a contratição estava errada, ou seja o dobro de x é divisivel por 4, portanto a tese é verdadeira, por isso retorno True

'''Prove por contrapositiva
 "Se 3n+2 é par, então n é par". '''
'''Tese'''
def ex6T(n):
    if (3*n+2)%2 ==0:
        if n%2==0:
            return True
    return False

'''Prava'''
def ex6Prova(n):
    if (3*n+2)%2 !=0:
        if n%2!=0:
            return False
    return True#a contrapositiva estava certa, por isso retorno True

print("Ex1: valores (2,2), resultado          {}           Ex1: valores (2,3), resultado           {} "
      "\nEx2: valores (2,2), resultado          {}          Ex2: valores (3,3), resultado           {}"
      "\nEx3: valores (2,2), resultado          {}          Ex3: valores (3,3), resultado           {}"
      "\nEx4 Tese : valores (2), resultado      {}          Ex4 Tese: valores (0), resultado        {}"
      "\nEx4 Prova : valores (2), resultado     {}           Ex4 Prova: valores (0), resultado       {}"
      "\nEx5 Tese : valores (12), resultado     {}           Ex5 Tese: valores (18), resultado       {}"
      "\nEx5 Prova : valores (12), resultado    {}           Ex5 Prova: valores (18), resultado      {}"
      "\nEx6 Tese : valores (1), resultado      {}          Ex6 Tese: valores (5), resultado        {}"
      "\nEx6 Prova : valores (1), resultado     {}          Ex6 Prova: valores (5), resultado       {}".format(ex1(2,2),ex1(2,3),
                                                                                             ex2(2,2),ex2(3,3),
                                                                                             ex3(2,2),ex3(3,3),
                                                                                             ex4T(2),ex4T(0),
                                                                                             ex4Prova(2), ex4Prova(0),
                                                                                             ex5T(12), ex5T(18),
                                                                                             ex5Prova(12), ex5Prova(18),
                                                                                             ex6T(1), ex6T(5),
                                                                                             ex6Prova(1), ex6Prova(5),
                                                                                     ))