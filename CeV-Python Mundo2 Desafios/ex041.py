# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de uma atleta e mostre sua categoria conforme a idade:
#  até 9 anos: mirim; até 14 anos: infantil; até 19 anos: junior; até 25 anos: sênior; acima: master

from datetime import date
ano = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano - nascimento
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

