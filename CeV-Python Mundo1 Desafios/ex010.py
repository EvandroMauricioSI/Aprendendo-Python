# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessa tem na carteira e mostre quantos dólares ela pode comprar.

realBR = float(input("Quantos R$ você tem na carteira? "))
dollar = realBR / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(realBR, dollar))
