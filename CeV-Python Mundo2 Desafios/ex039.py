# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar; Se é hora dele se alistar; Se já passou o tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou passou do prazo

import datetime

idade_alistamento = 18
data_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - data_nasc

if idade == idade_alistamento:
    print('Está na hora de se alistar')
elif idade < idade_alistamento:
    faltam = idade_alistamento-idade
    if faltam==1:
        print('Ainda falta {} ano para se alistar no serviço militar! '.format(faltam))
    else:
        print('Ainda faltam {} anos para se alistar no serviço militar! '.format(faltam))
else:
    passaram = idade - idade_alistamento
    if passaram==1:
        print('Já passou o tempo de alistamenta a {} ano'.format(passaram))
    else:
        print('Já passou o tempo de alistamenta a {} anos'.format(passaram))




