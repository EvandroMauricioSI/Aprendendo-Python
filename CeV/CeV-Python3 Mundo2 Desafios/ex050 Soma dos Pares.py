# Exercício 050: Soma dos pares:
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('num({}): '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} número(s) PAR(ES) e a soma = {}'.format(cont, n))
