import os

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

word = "abcda"
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
