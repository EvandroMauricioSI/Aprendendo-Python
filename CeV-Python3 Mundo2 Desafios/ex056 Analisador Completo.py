# Exercício 056: Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

somaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
mulherMenorDe20 = 0
for p in range(1, 5):
    print('------- {}ª Pessoa ------'.format(p))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mn' and idade>maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherMenorDe20 += 1

mediaIdade = somaIdade /4
print('A média da idade do grupo é {:.1f}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeMaisVelho))
print('Total de mulheres abaixo de 20 anos = {} '.format(mulherMenorDe20))