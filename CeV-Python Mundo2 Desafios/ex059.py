# Exercício 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair
# Seu programa deverá realizar a operação solicitada em casa caso

v1 = float(input('Digite o 1° valor: '))
v2 = float(input('Digite o 2° valor: '))

op = 0
while op !=5:
    op = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    :: '''))
    if op == 1:
        soma = v1 + v2
        print('{} + {} = {}'.format(v1, v2, soma))
    if op == 2:
        mult = v1 * v2
        print('{} + {} = {}'.format(v1, v2, mult))
    if op == 3:
        if v1 > v2:
            print('{} é maior que {}'.format(v1, v2))
        if v2 > v1:
            print('{} é maior que {}'.format(v2, v1))
        else:
            print('{} é igual a {}'.format(v1, v2))
    if op == 4:
        v1 = float(input('Digite o 1° valor: '))
        v2 = float(input('Digite o 2° valor: '))
    if op == 5:
        print('FIM')
    if op >5 :
        print('Opção inválida!')