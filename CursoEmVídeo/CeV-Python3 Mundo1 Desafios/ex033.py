# DESAFIO 033
# Faça um programa que leia 3 números e mostre qual é o MAIOR e qual é o MENOR

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z

print('Maior = {}'.format(maior))
print('Menor = {}'.format(menor))
