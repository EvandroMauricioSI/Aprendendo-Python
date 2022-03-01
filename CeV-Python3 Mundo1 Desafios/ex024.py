# DESAFIO 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

cidade = str(input('Em que cidade você nasceu: ')).strip()
cidade = cidade.upper()
div = cidade.split()
print('SANTO' in div[0])

# maneira mais simples
print(cidade[:5].upper()=='SANTO')