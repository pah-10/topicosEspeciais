#Elabore uma aplicação que receba o peso e altura de um número indeterminado de pessoas.
# Utilize tratamento de exceção para garantir que os valores informados são válidos.
# Após a entrada correta dos dados apresente o IMC.
# Para cada entrada de dados pergunte ao usuário “Deseja continuar?”

import os

#Função que limpa tela
def limpar_tela():
    os.system('cls')

#Função que verifica valores inseridos
def info_valor():
    while True:
        try:
            return float(input("Entre com o valor: "))
        except ValueError:
            print("O valor informado não é um número")

#Função que calcula o IMC
def imc(peso, altura):
    return round(peso / (altura * altura), 2)

#Função main
def main():
    limpar_tela() 

    continuar = True
    while continuar:

        print("\tPeso")
        peso = info_valor()

        print("\tAltura")
        altura = info_valor()

        IMC = imc(peso, altura)
        print (IMC)

        continuar = input("\n\nDesejar continuar calculando IMC? S/N: ")

        if (continuar == "S" or continuar == "s"):
            continuar = True
            limpar_tela() 
        else:
            continuar = False

#Chamada da função
main()
