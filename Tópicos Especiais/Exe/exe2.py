#Crie um programa para calcular e exibir na tela o peso ideal
import os
os.system('cls')

#entrada dos dados
altura = float(input("Informe a altura: "))
peso = float(input("Informe o peso: "))

IMC = (peso / (altura ** 2))

print(IMC)

#saida de dados
print("O IMC eh = {}".format(IMC))