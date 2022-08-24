#Faça uma aplicação que apresente em tela a tabuada de qualquer número.
#O usuário fornece o número desejado e a aplicação apresenta a relação de todos os cálculos de 1 a 10. 

import os
os.system('clear')

valor = int(input("Insira um valor para gerar a tabuada: "))

os.system('clear')
print("\tTabuada do {}\n".format(valor))

for i in range (1, 11):
	print("{} x {} = {}".format(i, valor, i * valor))
