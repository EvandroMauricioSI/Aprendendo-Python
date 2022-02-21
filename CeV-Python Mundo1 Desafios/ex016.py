# DESAFIO 016
#  Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela sua porção inteira.
'''
from math import trunc
num = float(input('Digite um número(REAL): '))
print('O valor digitado foi {} e a parte inteira é {} ' .format(num, trunc(num)))
'''

num = float(input('Digite um número(REAL): '))
print('O valor digitado foi {} e a parte inteira é {} ' .format(num, int(num)))
