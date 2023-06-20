nome = "jose"
idade = 12
peso = 30
souFeliz = True

print("Exibir uma String:  %s" %nome) #%s representa uma string. 
print("Exibir um Integer:  %d" %idade) #%d representa um número inteiro (integer).
print("Exibir um Float:    %f" %peso) #%f representa um número flutuante (float).
print("Exibir uma Boleana: %r" %souFeliz) #%r representa uma boleana (bool).
print("-----------------------------------------------------------------------")
import random #Importando a biblioteca
x = random.randint(1, 5) #Escolhendo entre um numero aleatiro entre (1 e 5)
print(x) #Printando o numero sortido