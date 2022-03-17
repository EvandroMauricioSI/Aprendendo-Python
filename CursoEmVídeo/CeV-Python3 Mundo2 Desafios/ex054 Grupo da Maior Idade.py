# Exercício 054: Grupo da Maior Idade
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for i in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano_atual-nascimento
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('São {} pessoas maiores de idade e {} pessoas menores de idade'.format(cont_maior, cont_menor))
