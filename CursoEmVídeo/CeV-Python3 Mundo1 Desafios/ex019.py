# DESAFIO 019
# Um professor que sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele
# lendo o nome deles e escrecendo o nome do escolhido

from random import choice
a = "João"
b = "Maria"
c = "Pedro"
d = "Paulo"
lista = [a, b, c, d]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
