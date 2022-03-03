# Exercício 94 – Unindo dicionários e listas.
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: (A) Quantas pessoas foram cadastradas (B) A média de idade
# (C) Uma lista com as mulheres (D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
p = list()
soma = media = 0
while True:
    # preenchendo dicionário
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome      : '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF': # para verificar se escolheu umra opção válida
            break
        print('ERRO! Digite apenas M ou F') #else implícito
    pessoa['Idade'] = int(input('Idade     : '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())  # copia todos os dados de pessoa
    while True:
        resp = str(input('Quer continuar [S/N]?: ')).upper()[0]
        if resp in 'SN': # para verificar se escolheu umra opção válida
            break
        print('ERRO! Digite apenas S ou N') #else implícito
    if resp in 'Nn':
        break
print('…'*50)
print(galera)

print('…'*50)
print(f'(A) Quantas pessoas foram cadastradas : {len(galera)}')

print('…'*50)
média = soma/len(galera)
print(f'(B) A média de idade ................ : {média:5.2f} anos')
print('…'*50)

print(f'(C) Uma lista com as mulheres ....... : ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f' -> {p["Nome"]}', end= ' ')
print()

print('…'*50)
print(f'(D) Pessoas com idade acima da média  : ')
for p in galera:
    if p['Idade'] > média:
        print('||', end=' ')
        for chave, valor in p.items():
            print(f'{chave:<5} = {valor:<7} |', end='')
        print('|')
print()

print('…'*50)
print('…'*50)
print('FIM:.^50')