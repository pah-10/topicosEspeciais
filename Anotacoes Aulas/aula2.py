#SLIDE 1

#lib os controla o console do sistema 
import os

"""

# os.system('clear') para linux
os.system('cls')

#Números decimais

import decimal

x = 23
y = 1.05
d = decimal.Decimal(23) / decimal.Decimal("1.05")

print(x / y)
print(d)

"""

#####################################################################

"""

# Concatenação de String
os.system('cls')

nome = 'Paola'
sobrenome = 'Capita'

nomeCompleto = nome,sobrenome
nomeCompleto2 = f"{nome}.{sobrenome}"

print(nomeCompleto)
print(nomeCompleto2)

funcaoFormatada = "{0} Olá Mundo {1}".format(('<'), ('>'))
print(funcaoFormatada)

"""

#####################################################################

"""

#Operações com string
os.system('cls')

string = "Paola Capita"

print(string[0])
print(string[-3])

print(string[2] * 7)

print(string[3:8])
print(string[:6])
print(string[6:])

print('n' in string)
print('z' not in string)

s = "paola "

print(s.capitalize())
print(s.upper())
print(s.lower())

print(len(s))
print(len(s.strip()))

"""

#####################################################################

"""

#Entrada e saida de dados
os.system('cls')

#entrada dos dados
#num1 = float(input("Informe o primeiro valor: "))
#num2 = float(input("Informe o segundo valor: "))

#soma = (num1 + num2)

#saida de dados
#print("Soma = %.2f" %soma)

str1 = "Paola Capita"

#imprime verticalmente
for c in str1:
    print(c)

#imprime horizontalmente
for c in str1:
    print(c, end = '\t')

"""

#####################################################################

#SLIDE 2

os.system("cls")

for i in range(5):
    if i == 3:
        continue

    print(i)

for i in range(5):
    if i == 3:
        break

    print(i)