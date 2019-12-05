#encoding: utf-8
nums = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def check_base(text, base):
    for letter in text:
        if not letter in nums[:base]:
            return False
    return True
# 0101010101010101010 = 174762
#  101010101010101010
def toDecimal(text, base):
    final = 0

    for letter in range(len(text)):
        index = text[len(text)-1-letter]
        if index == "F":
            index = 15
        elif index == "E":
            index = 14
        elif index == "D":
            index = 13
        elif index == "C":
            index = 12
        elif index == "B":
            index = 11
        elif index == "A":
            index = 10
        number = int(index) * (base ** letter)
        final += number

    return final

def toBase(text, base):
    final = ""
    remaining = int(text)

    while remaining > 0:
        number = remaining % base
        remaining = remaining // base
        if number == 15:
            number = "F"
        elif number == 14:
            number = "E"
        elif number == 13:
            number = "D"
        elif number == 12:
            number = "C"
        elif number == 11:
            number = "B"
        elif number == 10:
            number = "A"
        final += str(number)

    return final[::-1]

option = int(input("1. Converter de qualquer base para decimal\n2. Converter de decimal para qualquer base\n"))

while option != 1 and option != 2:
    option = int(input("1. Converter de qualquer base para decimal\n2. Converter de decimal para qualquer base\n"))

if option == 1:
    base = int(input("Digite a base (de 2 a 16): "))
    while base < 2 or base > 16:
        base = int(input("Digite a base (de 2 a 16): "))

    text = input("Digite um número válido na base " + str(base) + ": ")
    while not check_base(text, base):
        text = input("Entrada inválida.\nDigite um número válido na base " + str(base) + ": ")

    print(text + " convertido para a base decimal: " + str(toDecimal(text, base)))
else:
    base = int(input("Digite a base (de 2 a 16): "))
    while base < 2 or base > 16:
        base = int(input("Digite a base (de 2 a 16): "))

    text = input("Digite um número válido na base decimal: ")
    while not check_base(text, 10):
        text = input("Entrada inválida.\nDigite um número válido na base decimal: ")

    print(text + " convertido para a base " + str(base) +": " + str(toBase(text, base)))
