#Slide 3

"""
#tupla são tipos imutaveis, ou seja, não podem ser alterados
import os
import collections
os.system('cls')

#tuplas nomeadas
Pessoa = collections.namedtuple("Pessoa", "id nome idade email")

pessoas = []
pessoas.append(Pessoa(1, "João da Silva", 22, "joao@joao.com"))
pessoas.append(Pessoa(2, "Ana Maria", 19, "ana@ana.com.br"))

for p in pessoas:
    print("ID...: %d" %p.id)
    print("Nome.: %s" %p.nome)
    print("Idade: %d" %p.idade)
    print("Email: %s \n" %p.email)

"""

