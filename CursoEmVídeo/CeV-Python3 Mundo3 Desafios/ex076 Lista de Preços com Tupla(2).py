# Exercício 76: Lista de Preços com Tupla
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25, 'Tranferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print('{:^40}'.format( 'Lista de Preços' ))
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*40)