#SLIDE 2 try e def

import os

#Definições de funções
def limpar_tela():
    os.system('cls')

def ler_numero():
    return int(input("Informe o valor :"))

def soma(n1, n2):
    return n1 + n2

def main():
    limpar_tela()
    
    n1 = ler_numero()
    n2 = ler_numero()

    print(soma(n1, n2))


#chamada da funcao main para execução
main()