# -*- coding:utf-8 -*-
#Feito por Guilherme Solski Alves
from tkinter import *

canvas = Tk()
#variavel que salva os valores e realiza os calcula.
show = ""
#variavel que amarzena se tem um letra na equação, começa como true supondo que nao possue nenhuam letra já presente na mesma.
testedeVariavel = True
#varial do Entry, onde mostra o valor e pega input do teclado.
e = Entry(canvas,width=66,font=30)
e.place(x=0, y= 0)
#array com todas a letras do alfabeto para verificação.
NaoPodeTer = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
                  "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "U", "u",
                  "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]


#Função que adiciona o valor do botão pressionado ao Entry.
def Se_o_BotaoPresionado(num):
    #necessita estar como global para possiveis modificaçãoes em outras funçôes.
    global show
    global testedeVariavel
    #apada a mensagem de error ao clicar em um novo botao.
    if testedeVariavel == False:
        e.delete(0,END)
        testedeVariavel = True
    #adiciona o novo valor.
    show = e.get()
    show = show + str(num)
    #apaga o que tava mostrando antes e mostra a nova operação.
    e.delete(0,END)
    e.insert(0,show)


#função que faz o calculo da equação, e mostra no Entry.
def igual():
    #necessita estar como global para possiveis modificaçãoes em outras funçôes.
    global show
    global testedeVariavel
    #aplicação que evita possiveis erros.
    testedeVariavel = True
    #verificação se tem uma letra na calculavel na campo de digitação.
    for i in range(len(e.get())):
        if e.get()[i] in NaoPodeTer:
            testedeVariavel = False
            break
    #validação do testes.
    if testedeVariavel == False:
        e.delete(0, END)
        show = "Error"
        e.insert(0,show)
    else:
        #variavel que calcula atraves da string a partir da função eval
        total = eval(e.get())
        e.delete(0, END)
        e.insert(0, total)
        #zera a viral que guarda para iniciar nova operação
        show= ""

#Função que limpa o a variavel show.
def clear():
   global show
#zera a varialvel e limpa o Entry.
   show = ""
   e.delete(0, END)


# botoes numericos.

one = Button(canvas, text = "1", width=25,command=lambda:Se_o_BotaoPresionado(1)) #a lambda nesse caso evita que a função seja chamada no inico da aplicação.
one.grid(row = 4, column =0)

two = Button(canvas, text = "2", width=25,command=lambda:Se_o_BotaoPresionado(2))
two.grid(row = 4, column = 1)

three = Button(canvas, text = "3", width=25,command=lambda:Se_o_BotaoPresionado(3))
three.grid(row = 4, column = 2)

four = Button(canvas, text = "4", width=25,command=lambda:Se_o_BotaoPresionado(4))
four.grid(row = 3, column = 0)

five = Button(canvas, text = "5",width=25, command=lambda:Se_o_BotaoPresionado(5))
five.grid(row= 3, column = 1)

six = Button(canvas, text = "6", width=25,command=lambda:Se_o_BotaoPresionado(6))
six.grid(row = 3, column = 2)

seven = Button(canvas, text="7", width=25,command=lambda:Se_o_BotaoPresionado(7))
seven.grid(row = 2, column = 0)

eight = Button(canvas, text="8", width=25,command=lambda:Se_o_BotaoPresionado(8))
eight.grid(row = 2, column = 1)

nine = Button(canvas, text="9", width=25,command=lambda:Se_o_BotaoPresionado(9))
nine.grid(row = 2, column = 2)

zero = Button(canvas, text = "0", width=25,command=lambda:Se_o_BotaoPresionado(0))
zero.grid(row = 5, column = 0)

#Botoes de operadores.

soma = Button(canvas, text = "+", width=25,command=lambda:Se_o_BotaoPresionado("+"))
soma.grid(row = 2, column = 3)

menos = Button(canvas, text = "-", width=25,command=lambda:Se_o_BotaoPresionado("-"))
menos.grid(row = 3, column = 3)

div = Button(canvas, text = "/", width=25,command=lambda:Se_o_BotaoPresionado("/"))
div.grid(row = 4, column = 3)

mult = Button(canvas, text = "x", width=25 ,command=lambda:Se_o_BotaoPresionado("*"))
mult.grid(row = 5, column = 3)

raiz = Button(canvas, text = "Raiz quadrada", width=25,command=lambda:Se_o_BotaoPresionado("** (1/2)"))
raiz.grid(row =6, column = 1)

elevado = Button(canvas, text = "Elevado", width=25,command=lambda:Se_o_BotaoPresionado("**"))
elevado.grid(row =6, column = 0)

#Caracter especiais.

abreParenteses = Button(canvas, text = "(", width=25,command=lambda:Se_o_BotaoPresionado("("))
abreParenteses.grid(row = 5, column = 1)

fechaParenteses = Button(canvas, text = ")", width=25,command=lambda:Se_o_BotaoPresionado(")"))
fechaParenteses.grid(row = 5, column = 2)

ponto = Button(canvas, text = ".", width=25,command=lambda:Se_o_BotaoPresionado("."))
ponto.grid(row = 6, column = 2)

equal = Button(canvas, text = "=", width=25,command=igual) #Não se utiliza a lambda na hora de chamar a função pois não faz a diferença se a mesma é chamada no inicio da aplicação.
equal.grid(row = 6, column = 3)

limpa = Button(canvas, text = "C", width=25,command=clear)
limpa.grid(row = 1, column = 3)

#Implementação do lopin, do tamannho da tela e define o nome da aplicação.
canvas.geometry("712x175")
canvas.title("calculadora")
canvas.mainloop()