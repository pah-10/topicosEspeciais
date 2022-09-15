#Exercício 1: Escreva um programa em Python capaz de ler as primeiras n linhas de um arquivo texto. O número de linhas é informado pelo usuário.

import os

#Função que limpa console
def limpar_tela():
    os.system('cls')

#Função que valida valores inseridos
def info_valor():
    while True:
        try:
            return int(input("Entre com o valor: "))
        except ValueError:
            print("O valor informado não é um número inteiro")

def ler_linhas(qtd_linhas):
    arq = open("aqvBase.txt", "r")

    for i in range(qtd_linhas):
        linha = arq.readline()
        print(linha.strip("\n"))

    arq.close()

#Função principal
def main():

    limpar_tela() 
    qtd_linhas = info_valor()

    ler_linhas(qtd_linhas)

#Chamada da função principal
main()