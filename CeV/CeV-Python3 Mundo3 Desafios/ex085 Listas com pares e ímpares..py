# Exercício 085 – Listas com pares e ímpares.
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[],[]]
for i in range(1, 8):
    n = int(input(f'digite o {i}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Valores pares .... : {num[0]}')
print(f'Valores ímpares .. : {num[1]}')