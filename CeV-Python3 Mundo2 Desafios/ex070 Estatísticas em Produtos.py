# Exercício 070: Estatísticas em Produtos
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# (a) Qual é o total gasto na compra. (b) Quantos produtos custam mais de R$1000.
# (c) Qual o nome do produto mais barato.


print('-'*30)
print('Lista de Compras: ')
totalGasto = maisDeMil = maisBarato = cont = 0
nomeDoMaisBarato = ' '
while True:
    print('-' * 30)
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do Produto: '))

    cont += 1
    totalGasto += preço

    if preço > 1000:
        maisDeMil += 1

    if cont == 1 or preço < maisBarato:
        maisBarato = preço
        nomeDoMaisBarato = produto
    #else:
    #    if preço <= maisBarato:
    #        maisBarato = preço
    #        nomeDoMaisBarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Mais produtos? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('Fim das Compras! ')
print(f'(a) Qual é o total gasto na compra ............. {totalGasto}')
print(f'(b) Quantos produtos custam mais de R$1000 ..... {maisDeMil}')
print(f'(c) Qual o nome do produto mais barato ......... {nomeDoMaisBarato}')



