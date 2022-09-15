# Faça um programa que leia um vetor de 15 posições de números inteiros e divida todos os elementos pelo maior valor do vetor.

import os
import collections

def limpar_tela():
	os.system('cls')

def info_valor(contador):
    while True:
        try:
            return int(input("Entre com o %dº valor : " %contador))
        except ValueError:
            print("O valor informado não é um número inteiro")

def insercao_valores():
    dados_valores = []

    for i in range(1, 16):
        valor = info_valor(i)

        dados_valores.append(valor)
  
    return dados_valores				

def calculo(lista_valores):
	
	for i in range(15):
		lista_valores[i] = lista_valores[i]/max(lista_valores)

	print(lista_valores)

def main():
	limpar_tela() 

	valores = insercao_valores()

	print("Maior valor: ",max(valores))

	calculo(valores)

main()
