# NP1 Tópicos Especiais
# Paola Paulina de Jesus Santa Capita
# RA: 2840482011007

import os
import json

def limpa_tela():
    os.system("cls") 

def menu():
    print('''\t\tVarejão do João\t\n
MENU:
    [1] - Cadastrar de Produto
    [2] - Relatório de Produtos
    [3] - Relatório de Estoque Baixo
    [4] - Exportar Dados
    [0] - Sair
    ''')

    print("Escolha uma opção:")
    opcao = verifica_entrada_numero_inteiro()
    
    return opcao

def verifica_entrada_numero():
    while True:
        try:
            return float(input("Informe o valor do produto:\n"))
        except ValueError:
            print("O valor informado não é um númeron tente novamente:")

def verifica_entrada_numero_inteiro():
    while True:
        try:
            return int(input(" "))
        except ValueError:
            print("O valor informado não é um número inteiro, tente novamente:")

def cadastrar_produto(lista_produtos):
    #recebendo dados
    nome = (input("Informe o nome do produto:\n"))
    valor_compra = verifica_entrada_numero()
    print("Informe a quantidade em estoque do produto:")
    qtd = verifica_entrada_numero_inteiro()
    id = gera_cod(lista_produtos)
    valor_venda = valor_compra * 1.25

    #atribuindo no dicionário
    dados = {'Codigo': id, 'Nome':  nome.upper() , 'Valor_Compra': valor_compra, 'Valor_Venda': valor_venda, 'Quantidade': qtd}

    #juntando na lista dos produtos
    lista_produtos.append(dados)

    return lista_produtos

def gera_cod(lista_produtos):
    ultimo_produto = len(lista_produtos)-1

    if ultimo_produto == -1:
        return 1
    else:
        id = lista_produtos[ultimo_produto].get('Codigo')
        return (id + 1)

def relatorio_produtos(lista_produtos):
    ultimo_produto = len(lista_produtos)-1

    if ultimo_produto == -1:
        return print("\t\tSem produtos Cadastrados\t\n")
    else:
        #orena lista pelas chaves do dicionario alfabeticamente
        lista_ordenada = sorted(lista_produtos, key=lambda dicionario: dicionario['Nome'])
        #print(lista_ordenada)

        print("\t\tRelatório de Produtos\t\n")

        for item in lista_ordenada:
            print(f"Código {item['Codigo']}, Nome {item['Nome']}, Valor de Compra {item['Valor_Compra']}, Valor de Venda {item['Valor_Venda']}, Quantidade {item['Quantidade']}")    

def relatorio_estoque_baixo(lista_produtos):
    ultimo_produto = len(lista_produtos)-1

    if ultimo_produto == -1:
        return print("\t\tSem produtos Cadastrados\t\n")
    else:
        print("\t\tRelatório de Estoque Baixo\t\n")

        for item in lista_produtos:
            if(item['Quantidade'] < 6):
                print(f"Código {item['Codigo']}, Nome {item['Nome']}, Valor de Compra {item['Valor_Compra']}, Valor de Venda {item['Valor_Venda']}, Quantidade {item['Quantidade']}")    

def exportar_dados(lista_produtos):
    #O arquivo deve ser criado dentro de uma pasta arquivo na raiz onde o aplicativo está rodando
    #Certifique-se que esta pasta exista ou verifique onde o aplicativo está rodando
    arqv = open("arquivo/dados.json","w", encoding= "utf-8")
    json.dump(lista_produtos, arqv, sort_keys = True, indent = 4, ensure_ascii = False)
    arqv.close

    print("\t\tArquivo dados.json criado dentro da pasta arquivo\t\n")


#Execução do código
lista_produtos = []

while True:
    limpa_tela()
    opcao_user = menu()

    if(opcao_user == 0):
        break
    elif(opcao_user == 1):
        cadastrar_produto(lista_produtos)
        print("\n")
        os.system("pause")
    elif(opcao_user == 2):
        relatorio_produtos(lista_produtos)
        print("\n")
        os.system("pause")
    elif(opcao_user == 3):
        relatorio_estoque_baixo(lista_produtos)
        print("\n")
        os.system("pause")
    elif(opcao_user == 4):
        exportar_dados(lista_produtos)
        print("\n")
        os.system("pause")
    else:
        print("Opção Inválida")
