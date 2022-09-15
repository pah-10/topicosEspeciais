# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Example
#  For inputArray= [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21.
#  7 and 3 produce the largest product.

import os
import collections

os.system("cls")

def adjacentElementsProduct(lista):
	largest_product = lista[0] * lista[1]
	
	for i in range(len(lista)-1):
		if(largest_product < (lista[i] * lista[i + 1])):
			largest_product = lista[i] * lista[i + 1]
	
	return largest_product

inputArray= [3, 6, -2, -5, 7, 3]

print("O maior produto eh", adjacentElementsProduct(inputArray)) 