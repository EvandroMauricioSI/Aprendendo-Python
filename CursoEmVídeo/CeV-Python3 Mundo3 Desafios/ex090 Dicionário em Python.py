# Exercício 90 – Dicionário em Python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome Aluno: '))
#aluno['Média'] = float(input('Média Aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 4:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'

print('= '*15)
for chave, valor in aluno.items():
    print(f'{chave:.<15}: {valor}')
print('= '*15)