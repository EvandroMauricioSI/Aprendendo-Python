# DESAFIO 22
# Crie um progrma que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas
# b) O nome com todas as letras minúsculas
# c) Total de letras sem considerar espaço
# d) Quantas letras tem o primeiro nome

nome = str(input('informe seu nome completo: ')).strip()
print('Mostre: ')
print('a) O nome com todas as letras maiúsculas:  {}'.format(nome.upper()))
print('b) O nome com todas as letras minúsculas:  {}'.format(nome.lower()))
print('c) Total de letras sem considerar espaço:  {} letras'.format(len(nome)-nome.count(' ')))
print('d) Quantas letras tem o primeiro nome   :  {} letras'.format(nome.find(' ')))

separa = nome.split()
print('\n\nSeu primeiro nome é {}  e ele tem  {} letras: '.format(separa[0], len(separa[0])))