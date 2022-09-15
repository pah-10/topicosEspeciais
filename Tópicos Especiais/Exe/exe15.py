#Create a function checkPalindromethatgiven the string, check if it is a palindrome.
# Example
#   For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
#   For inputString= "abac", the output should be checkPalindrome(inputString) = false;
#   For inputString= "a", the output should be checkPalindrome(inputString) = true.

import os
os.system('cls')

def checkPalindrome(string):
	if str(string) == str(string)[::-1] :
		print("Eh palindromo")
	else:
		print("Nao eh palindromo")

palavra = input("Insira a palavra para verificação: ")

checkPalindrome(palavra.lower())