# Exercício 074: Maior e menor valores em Tupla.
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint
num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(num)
maior = menor = num[0]

for i in range(0, 5):
    if maior < num[i]:
        maior = num[i]
    if menor > num[i]:
        menor = num[i]
print(f'Maior = {maior} e Menor = {menor}')

