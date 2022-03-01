# Exercício 87 – Mais sobre Matriz em Python.
# Aprimore o desafio anterior, mostrando no final: (A) A soma de todos os valores pares digitados.
# (B) A soma dos valores da terceira coluna. (C) O maior valor da segunda linha.

matriz = [[], [], []]
somaPar = maiorDaColuna2 = somaColuna3 = 0

# Preencher a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'informe o valor para m[{linha}][{coluna}]]: ')))

# Somar os elementos pares da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]

# Somar os elementos da terceira coluna
for linha in range(0, 3):
    somaColuna3 += matriz[linha][2]

# Encontrar o maior valor da segunda linha
for coluna in range(0, 3):
    if coluna == 0:
        maiorDaColuna2 = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maiorDaColuna2:
            maiorDaColuna2 = matriz[1][coluna]

# Exibir a matriz na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'| {matriz[linha][coluna]:^5}', end=' ')
    print('|')

print(f'(A) A soma de todos os valores pares digitados .... = {somaPar}')
print(f'(B) A soma dos valores da terceira coluna ......... = {somaColuna3}')
print(f'(C) O maior valor da segunda  ..................... = {maiorDaColuna2}')