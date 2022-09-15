#Exercício 3: Escreva um programa capaz de contar a frequência de palavras em um arquivo.

import os

#Função que limpa console
def limpar_tela():
    os.system('cls')

def conta_freq(palavra):
    arq = open("aqvBase.txt", "r")

    for i in range(arq):
        if
        linha = arq.readline()
        print(linha.strip("\n"))

    arq.close()

#Função principal
def main():

    limpar_tela() 
    palavra = input("Informe a palavra que deseja pesquisar: ")

    conta_freq(palavra)

#Chamada da função principal
main()