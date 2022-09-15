#Uma imagem é formada por pixels. Considere uma imagem com dimensão de 10 x 10 e faça uma aplicação que contenha um estrutura bidimensional com essas dimensões. 
# A seguir, para cada posição da estrutura bidimensional armazene um valor aleatório entre 0 e 255 (esses valores correspondem às tonalidades aplicadas sobre a imagem). 
# Apresente em tela os valores gerados. 
import random 

img = [[random.randint(0,256) for j in range(10)] for i in range(10)]

print("Os valores gerados para a matrix 10X10 foram:")

for i in range(0, 10):
    print(img[i])