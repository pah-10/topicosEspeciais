#Faça um programa que receba o nome e duas notas de seis alunos e mostre de acordo com o relatório

import os
import collections

#tuplas nomeadas
Grades = collections.namedtuple("Grades", "nome nota1 nota2")

alunos = []
alunos.append(Grades("Paola", 10, 10)) #aprovado
alunos.append(Grades("Paulina", 4, 7)) #exame
alunos.append(Grades("De", 4, 5)) #exame
alunos.append(Grades("Jesus", 0, 0)) #reprovado
alunos.append(Grades("Santa", 8, 6)) #aprovado
alunos.append(Grades("Capita", -10, 0)) #reprovado

media = []
for p in alunos:
    media.append(p.nota1)
    media.append(p.nota2)

print("A media da classe eh: {}".format((sum(media))/len(alunos)))

aprovados = [i for i in alunos
                if(((i.nota1 + i.nota2)/2) > 6)]

print("Existe(m) {} aprovado(s)".format(len(aprovados)))

exame = [i for i in alunos
                if(((i.nota1 + i.nota2)/2) < 6 and ((i.nota1 + i.nota2)/2) >= 4)]

print("Existe(m) {} em exame(s)".format(len(exame)))

reprovados = [i for i in alunos
                if(((i.nota1 + i.nota2)/2) < 4)]

print("Existe(m) {} reprovado(s)".format(len(reprovados)))