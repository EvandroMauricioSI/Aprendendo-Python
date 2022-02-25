# Exercício 063: Sequência de Fibonacci v1.0
# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex.: 0, 1, 1, 2, 3, 5, 8

n = int(input('N? : '))
n1, n2 = 0, 1
c = 0
if n <= 0: print('Favor informar um valor POSITIVO não nulo!')
elif n == 1: print(n)
else:
    while c < n:
        print(n1, end=' -> ')
        x = n1 + n2
        n1 = n2
        n2 = x
        c += 1
print('Fim')
