import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def printWord(s):
    for i in s:
        print("_" if i == None else i, end=" ")
def getPos(l,w):
    return [i for i in range(len(w)) if w[i] == l]
def setInPos(a,p,l):
    for i in p:
        a[i] = l
    return a
def randomWord(t):
    lista_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return "".join([lista_char[random.randint(0,len(lista_char))] for i in range(t)])
word = randomWord(5)
Input_word,end,erros = [None for i in range(len(word))],0,0
while end < len(word) and erros < len(word):
    cls()
    printWord(Input_word)
    print("       Erros: {}".format(end))
    letter = input("")[0]
    if letter in word and letter not in Input_word:
        Input_word = setInPos(Input_word,getPos(letter,word),letter)
        erros += word.count(letter)  
    else:
        end += 1
print("morreu") if end > erros else print("ganhou")
