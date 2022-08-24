#Elabore uma aplicação que receba o nome de um produto e o seu valor. O desconto deve ser calculado de acordo com o valor fornecido conforme a Tabela.
#Apresente em tela o nome do produto, valor original do produto e o novo valor depois de ser realizado o desconto. Caso o valor digitado seja menor que zero, deve ser emitida uma mensagem de aviso. 

import os
os.system('cls')

#variaveis aux
desconto = 0
valorDescontado = 0

#entrada dos dados
nome = input("Informe o nome do produto: ")
valor = float(input("Informe o valor do produto: "))

if (valor < 0 or valor < 50):
	print("O valor inserido eh invalido! \nDigite APENAS produtos que tenham valores maiores que $50")
else:
	if (valor >= 50 and valor < 200):
		desconto = 5
	elif (valor >= 200 and valor < 500):
		desconto = 6
	elif (valor >= 500 and valor < 1000):
		desconto = 7
	elif (valor >= 1000):
		desconto = 8
		
	valorDescontado = (valor - ((valor * desconto) / 100))
	#saida de dados
	print("\nO produto {0} com valor original de ${1} passa a valer ${2} com desconto de {3}%".format(nome, valor, round(valorDescontado,2), desconto))
