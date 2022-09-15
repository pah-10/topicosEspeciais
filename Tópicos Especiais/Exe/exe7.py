# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second -from the year 101 up to and including the year 200, etc.
# Lógica utilizada: https://www.bing.com/search?q=como+converter+anos+em+séculos&cvid=6006cc1247034f1db7f8a612ed7a729b&aqs=edge.1.69i57j0l2.5496j0j9&FORM=ANAB01&PC=U531

import os
os.system('cls')

ano = input("Insira um ano (Utilize as 4 casas do ano, por exemplo 2002): ")

if (ano[2:4] == '00'):
	print("\n Seculo {}{}".format(ano[0], ano[1]))
else:
	print("\n Seculo {}".format(int(ano[0:2]) + 1))