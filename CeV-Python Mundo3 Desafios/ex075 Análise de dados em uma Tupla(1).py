# Exercício 75: Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre: (a) Quantas vezes apareceu o valor 9.
# (b) Em que posição foi digitado o primeiro valor 3. (c) Quais foram os números pares.

n = (int(input(f'Informe um valor:  ')), int(input(f'Informe um valor:  ')),
     int(input(f'Informe um valor:  ')), int(input(f'Informe um valor:  ')))
cont9 = 0
for i in range(0, 4):
    if n[i] == 9:
        cont9 += 1
print(f'(a) quantas vezes apareceu o valor 9 ................. : {cont9}x')
print('(b) em que posição foi digitado o primeiro valor 3 ... :', n.index(3))
print('(c) quais foram os números pares ..................... : ', end='')
for i in range(0, 4):
    if n[i]%2 == 0:
        print(n[i], end=' ')
