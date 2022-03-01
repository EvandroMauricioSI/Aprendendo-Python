# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
a = float(input('Informe o valor do ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O ângulo de  {:.2f} tem SIN  de {:.2f} '.format(a, seno))
print('O ângulo de  {:.2f} tem COS  de {:.2f} '.format(a, cosseno))
print('O ângulo de  {:.2f} tem TAN  de {:.2f} '.format(a, tangente))
