# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Preço do produto: "))
print('Novo preço com desconto = R$ {}'.format(preco - (preco*0.05)))