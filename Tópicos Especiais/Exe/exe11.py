# Lista

# Faça um programa que carregue um vetor de seis elementos numéricos inteiros, calcule e mostre:
# A quantidade de números pares
# Quais números são ímpares
# A soma dos números
# O maior número
# O menor número
# A quantidade de números positivos

import os
import collections

#Função que limpa console
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

    for i in range(1, 7):
        valor = info_valor(i)

        dados_valores.append(valor)
  
    return dados_valores

#Função que verifica se o número é par
def par(valor):
    return (valor % 2 == 0)

#Função que conta quantos pares existem
def qtd_pares(numeros):
    qtd_par = 0

    for i in numeros:
        if (par(i) == True):
            qtd_par += 1

    return qtd_par

#Função que retorna numeros impares
def retorna_impar(numeros):
    impares = []

    for i in numeros:
        if (i % 2 != 0):
            impares.append(i)

    return impares

def qtd_positivo(numeros):
    positivo = 0

    for i in numeros:
        if (i >= 0):
            positivo += 1

    return positivo

def main():
    limpar_tela() 
    lista_valores = insercao_valores()

    print("Existe(m) {} valor(es) par(es)".format(qtd_pares(lista_valores)))
    print("O(s) valor(es) impar(es) sao {}".format(retorna_impar(lista_valores)))
    print("A soma dos valores da lista eh: {}".format(sum(lista_valores)))
    print("O maior valor da lista eh: {}".format(max(lista_valores)))
    print("O menor valor da lista eh: {}".format(min(lista_valores)))
    print("Existe(m) {} valor(es) positivo(s)".format(qtd_positivo(lista_valores)))

main()