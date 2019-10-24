a = str(input('Entre com um texto: '))

list = a.replace("?","%#$").replace("!","%#$").replace(":?","%#$").replace(".","%#$").replace("...","%#$").replace("etc","%#$").strip().split("%#$")

list = [item.strip() for item in list]
print(list)
