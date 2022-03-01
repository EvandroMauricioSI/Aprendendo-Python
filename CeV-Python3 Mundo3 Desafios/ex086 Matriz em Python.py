# Exercício 86 – Matriz em Python.
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'informe o valor para m[{i}][{j}]]: ')))


for i in range(0, 3):
    for j in range(0, 3):
        print(f'| {matriz[i][j]:^5}', end=' ')
    print('|')

