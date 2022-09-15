#Uma farmácia precisa ajustar os preços de seus produtos em 12%. Elabore uma aplicação que receba o valor do produto e aplique o percentual de acréscimo.
#O novo valor a ser calculado deve ser arredondado e apresentado com duas casas decimais.

import os
os.system('cls')

#entrada dos dados
prod = float(input("Informe o valor do produto: "))
taxa = 1 + (12/100)

acrescimo = (prod * taxa)

#saida de dados
print("O valor mais 12% eh = {}".format(round(acrescimo,2)))