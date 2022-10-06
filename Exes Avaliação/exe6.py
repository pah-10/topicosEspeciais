# NP1 Tópicos Especiais
# Paola Paulina de Jesus Santa Capita
# RA: 2840482011007

import os
from datetime import datetime 

def limpa_tela():
    os.system("cls") 

def converte_mes_nome(mes):
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
	
    return meses[(mes - 1)]

def data_sistema():
	return datetime.now() 

limpa_tela()

data = data_sistema()

print("\t\tManipulação de Datas\t\t\n")
print ("Data atual do sistema: {}".format(data))

print (f"\nAno atual: {data.year}") 
print (f"Mês atual: {data.month}") 
print (f"Dia atual: {data.day}\n") 

print (f"Data atual formatada em dia/mês/ano: {data.day}/{data.month}/{data.year}")
print (data.strftime("Data atual formatada com strftime em dia/mês/ano: %d/%m/%Y\n"))

print (f"Data atual formatada com converte_mes_nome em dia de mês_por_extenso de ano: dia {data.day} de {converte_mes_nome(data.month)} de {data.year}")
print (data.strftime("Data atual formatada com strftime em dia de mês_por_extenso de ano: dia %d de %B de %Y"))