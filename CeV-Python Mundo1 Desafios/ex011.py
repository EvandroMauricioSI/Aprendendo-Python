# DESAFIO 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pinta-la
# sabendo que cada litro de tinta pinta 2m2.

L = float(input('Largura: '))
H = float(input('Altura : '))
area = L * H
tinta = area/2

print('Área = {}, serão necessários {} litros de tintas para pinta-la'.format(area, tinta))