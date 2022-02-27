# Exercício 069: Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: (a) Quantas pessoas tem mais de 18 anos. (b) Quantos homens foram cadastrados
# (c) Quantas mulheres tem menos de 20 anos.

print('-'*30)
print('Cadastro de pessoas')
homens = mulheresMenos20 = pessoasMaior18 = 0
while True:
    print('-' * 30)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        pessoasMaior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-'*30)
print(f'(a) Pessoas com mais de 18 anos ............. = {pessoasMaior18}')
print(f'(b) Quantos homens foram cadastrados ........ = {homens}')
print(f'(c) Quantas mulheres tem menos de 20 anos ... = {mulheresMenos20}')
print('Abacou! ')