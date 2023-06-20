lista = []

qntd = int(input("Escrava quantas palavras você vai colocar: "))
for i in range(qntd):
    string = input("Escreva as palavras: ")
    if string[0] in "a":
        lista.append(string)

print(lista)