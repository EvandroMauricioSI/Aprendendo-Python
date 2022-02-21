# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
a = "João"
b = "Maria"
c = "Pedro"
d = "Paulo"
lista = [a, b, c, d]
escolhido = shuffle(lista)
print('A ordem será: {}'.format(lista))
