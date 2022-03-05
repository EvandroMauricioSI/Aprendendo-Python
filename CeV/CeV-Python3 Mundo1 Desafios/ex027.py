# DESAFIO 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

n = str(input('informe o nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]).upper())
print('Último nome  : {}'.format(nome[len(nome)-1]).upper())
