# DESAFIO 017
# Faça um programa que leia o comprimeito do cateto e do cateto adjacento do triângulo
# retântulo calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt, hypot
cat_adj = float(input('informe o cateto adjacente : '))
cat_opo = float(input('informe o cateto oposto    : '))
# sem importar a classe math
hip1 = (cat_adj**2 + cat_opo**2) ** ( 1 / 2 )

# usando sqrt e pow da classe math
hip2 = sqrt(pow(cat_adj, 2)+pow(cat_opo, 2))

# uusando hypot da classe math
hip3 = hypot(cat_adj, cat_opo)

print('Hipotenusa (calc 1) = {:.2f}'.format(hip1))
print('Hipotenusa (calc 2) = {:.2f}'.format(hip2))
print('Hipotenusa (calc 3) = {:.2f}'.format(hip3))