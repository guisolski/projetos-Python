#dados serão inteiros
def insere(l,v):
    chave = v % len(l)
    l[chave] = v
    return  l
def pega(l,v):
    chave = v % len(l)
    print("valor achado",l[chave])

m = input("entre com o tamnho ")
i = True
#(chave, valor)
l = []
for i in range(int(m)):
    l.append(0)

while (i):
    escolha = int(input("escolha sua ação (1- sair, 2 - entre com o valor 3 - pegue um valor) "))
    if escolha == 1:
        i = False
    elif escolha == 2:
        v = int(input("entre com o valor "))
        l = insere(l,v)
    elif escolha == 3:
        v = int(input("entre com o valor "))
        pega(l,v)
    else:
        print("ecolha errada")