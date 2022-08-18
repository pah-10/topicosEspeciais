#Crie uma aplicação que receba o valor da base e da altura de um triângulo retângulo e apresente na tela sua área.
import os
os.system('cls')

#entrada dos dados
base = float(input("Informe o valor da base do triangulo: "))
altura = float(input("Informe o valor da altura do triangulo: "))

area = ((base * altura) / 2)

#saida de dados
print("A area do triangulo retangulo eh = {}".format(area))