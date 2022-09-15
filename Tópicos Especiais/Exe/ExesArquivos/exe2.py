# Exercício 2: Escreva um programa que realiza a leitura um arquivo e armazena o conteúdo em uma lista.

import os
os.system('cls')

arq = open("aqvBase.txt", "r")

arq.seek(0)
lista = arq.readlines()
print(lista)

arq.close()