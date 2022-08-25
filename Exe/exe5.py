#Na área da eletrônica, em um circuito em série temos que a resistência equivalente (total) desse circuito é obtida mediante a soma de todas as resistências existentes (RE = r1 + r2 + ... + rn).
#Faça uma aplicação que receba o valor de quatro resistências ligadas em série, calcule e mostre a resistência equivalente, a maior e a menor resistência. 

import os
os.system('cls')

#variaveis aux
resisEquivalente = 0
resisMaior = 0
resisMenor = 0

for i in range (4):
	#entrada dos dados
	resis = int(input("Informe o valor da resistencia: "))

	if (i == 0):
		resisMaior = resis
		resisMenor = resis
	else:
		if (resisMaior < resis):
			resisMaior = resis
		elif (resisMenor > resis):
			resisMenor = resis

	resisEquivalente += resis

#saida de dados
print("\nA resistencia equivalente eh: {0}\nA maior resistencia eh: {1}\nA menor resistencia eh: {2}".format(resisEquivalente, resisMaior, resisMenor))
