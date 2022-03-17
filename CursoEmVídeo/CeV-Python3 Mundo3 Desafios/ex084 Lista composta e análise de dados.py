# Exercício 084: Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# (a) Quantas pessoas foram cadastradas. (b) Uma listagem com as pessoas mais pesadas.
# (c) Uma listagem com as pessoas mais leves.

temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = 0
    else:
        if temp[1]>maior:
            maior = temp[1]
        if temp[1]<menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [s/n]: ')).lower().strip()[0]
    if resp in 'Nn':
        break
print('… '*30)
print(princ)
print('… '*30)
print(f'(a) Quantas pessoas foram cadastradas? R.: {len(princ)}')
print('… '*30)
print(f'(b) Uma listagem com as pessoas mais pesadas ')
print(f'O maior peso informado foi {maior}kg. Peso de: ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print('… '*30)
print(f'(c) Uma listagem com as pessoas mais leves')
print(f'O maior peso informado foi {maior}kg. Peso de: ', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
print('… '*30)
print('FIM')
print('… '*30)