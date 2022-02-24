# Exercício 052: Números Primos
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
n = int(input('Informe um valor: '))
for i in range(1, n+1):
    if n % i == 0:
        print('\033[1:32m', end=' ')
        cont += 1
    else:
        print('\033[1:31m', end=' ')
    print(i, end='')
if cont == 2:
    print('\nO número {} É PRIMO'.format(n))
else:
    print('\nO número {} NÃO É PRIMO'.format(n))
