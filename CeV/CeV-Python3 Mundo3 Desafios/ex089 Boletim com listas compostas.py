# Exercício 084: Boletim com listas compostas.
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
# mostrar as notas de cada aluno individualmente.

ficha = list()  # criando uma lista chamada ficha
# preenchendo a lista com vários elementos
while True:
    nome = str(input('Nome: '))            # ficha[0]
    nota1 = float(input('Nota1 : '))       # ficha[0[1[0]]]
    nota2 = float(input('Nota2 : '))       # ficha[0[1[1]]]
    media = (nota1+nota2)/2                # ficha[0]
    ficha.append([nome, [nota1, nota2], media])     # colocando os dados no índica na lista 'ficha'
    resp = str(input('quer continuar? [s/n]: '))    # add ou não mais elementos na lista
                        # se sim o índice da ficha passa de 0 para 1 e assim por diante
    if resp in 'Nn':
        break
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)   # só perfumaria
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 26)     # mais perfumaria
    op = int(input('Mostras notas de qual aluno? [999 pra sair]: '))
    if op == 999:
        break
    if op <= len(ficha)-1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')