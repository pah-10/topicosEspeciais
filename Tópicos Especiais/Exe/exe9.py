# Elabore uma aplicação que receba o peso e altura de um número indeterminado de pessoas.
# Utilize tratamento de exceção para garantir que os valores informados são válidos.
# Após a entrada correta dos dados apresente o IMC.
# Para cada entrada de dados pergunte ao usuário “Deseja continuar?”

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

#Função que faz a inserção dos dados
def insercao_valores():
    dados_valores = []
    continuar = True

    while continuar:
        valor = info_valor()

        dados_valores.append(valor)

        continuar = input("\nDesejar continuar inserindo dados? S/N: ")

        if (continuar == "S" or continuar == "s"):
            continuar = True
            limpar_tela() 
        else:
            continuar = False
    
    return dados_valores

#Função que verifica se o número é par
def par(valor):
    return (valor % 2 == 0)

#Função que conta quantos pares existem
def conta_par(numeros):
    qtd_par = 0

    for i in numeros:
        if (par(i) == True):
            qtd_par += 1

    return qtd_par

#Função que verifica se o número é impar
def impar(valor):
    return (valor % 2 != 0)

#Função que retorna numeros impares
def retorna_impar(numeros):
    impares = []

    for i in numeros:
        if (impar(i) == True):
            impares.append(i)

    return impares

#Função que retorna maio numero
def maior_num(numeros):
    maior = numeros[0]

    for i in numeros:
        if (maior < i):
            maior = i

    return maior

#Função que retona menor numero
def menor_num(numeros):
    menor = numeros[0]

    for i in numeros:
        if (menor > i):
            menor = i

    return menor

#Função que retorna media de valores
def media_num(numeros):
    return (sum(numeros) / len(numeros))

#Função principal
def main():

    limpar_tela() 
    lista_valores = insercao_valores()

    print("\nOs valores inseridos foram: {} \n".format(lista_valores))
    print("Existe(m) {} valor(es) par(es)".format(conta_par(lista_valores)))
    print("O(s) valor(es) impar(es) sao {}".format(retorna_impar(lista_valores)))
    print("O maior numero eh {}".format(maior_num(lista_valores)))
    print("O menor numero eh {}".format(menor_num(lista_valores)))
    print("A media dos numero eh {}".format(media_num(lista_valores)))

#Chamada da função principal
main()