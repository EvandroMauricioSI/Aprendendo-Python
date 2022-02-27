# Exercício 75: Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre: (a) Quantas vezes apareceu o valor 9.
# (b) Em que posição foi digitado o primeiro valor 3. (c) Quais foram os números pares.

n = (int(input(f'Informe um valor:  ')), int(input(f'Informe um valor:  ')),
     int(input(f'Informe um valor:  ')), int(input(f'Informe um valor:  ')))
if 9 in n:
    print(f'(a) o valor 9 apareceu {n.count(9)}x')
else:
    print('(a) o valor 9 não foi digitado!')
if 3 in n:
    print(f'(b) valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('(b) O valor 3 não apareceu em nenhuma posição!')
print('(c) os valores pares digitados foram: ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')
