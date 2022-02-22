# Exercício 039: Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar; Se é hora dele se alistar; Se já passou o tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou passou do prazo

import datetime
ano_atual = datetime.date.today().year
alistamento = 18

nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
print('Quem nasceu em {} faz {} anos em {}'.format(nascimento, idade, ano_atual))

if idade == alistamento:
    print('Está na hora de se alistar')
elif idade < alistamento:
    faltam = alistamento - idade
    print('Ainda falta(m) {} ano(s) para se alistar no serviço militar! '.format(faltam))
    print('Você deve se alistar em {}'.format(ano_atual+faltam))
else:
    passaram = idade - alistamento
    print('Já passou o tempo de alistamento a {} ano(s)'.format(passaram))
    print('Você deveria ter se alistado em {}'.format(ano_atual - passaram))





