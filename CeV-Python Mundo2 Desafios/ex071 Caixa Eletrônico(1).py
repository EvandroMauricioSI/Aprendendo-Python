# Exercício 071: Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas células de cada valor serão entregues.
# OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valorSacado = int(input('\033[7:32m{:^30}\033[m  R$: '.format('Valor a ser sacado')))
print( )
while valorSacado != 0:
    cédulas = valorSacado // 50
    if cédulas >= 1:
        print(f'{cédulas:^4} Nota(s) de R$ 50,00')
    valorSacado = valorSacado%50

    cédulas = valorSacado // 20
    if cédulas >= 1:
        print(f'{cédulas:^4} Nota(s) de R$ 20,00')
    valorSacado = valorSacado % 20

    cédulas = valorSacado // 10
    if cédulas >= 1:
        print(f'{cédulas:^4} Nota(s) de R$ 10,00')
    valorSacado = valorSacado % 10

    cédulas = valorSacado // 1
    if cédulas >= 1:
        print(f'{cédulas:^4} Nota(s) de R$  1,00')
    valorSacado = valorSacado % 1
print('')
print('\033[7:31m{:^30}\033[m'.format('FIM'))