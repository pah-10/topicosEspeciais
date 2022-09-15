#Faça um programa que receba o nome de cinco produtos e seus precos e calcule:
#a qtd de produtos menores que 50, entre 50 e 100 e maior que 100

import os
import collections

#tuplas nomeadas
Produtos = collections.namedtuple("Produtos", "nome preco")

estoque = []
estoque.append(Produtos("Prod1", 10)) #inferior
estoque.append(Produtos("Prod2", 4)) #inferior
estoque.append(Produtos("Prod3", 50)) #entre
estoque.append(Produtos("Prod4", 100)) #entre
estoque.append(Produtos("Prod5", 1000)) #acima

inferior = [i for i in estoque
                if(i.preco < 50)]

print("Existe(m) produto(s) {} com preco inferior".format(len(inferior)))

entre = [i for i in estoque
                if(i.preco <= 100 and i.preco >= 50)]

print("Existe(m) produto(s) {} com preco entre".format(len(entre)))

acima = [i for i in estoque
                if(i.preco > 100)]

print("Existe(m) produto(s) {} com preco acima".format(len(acima)))