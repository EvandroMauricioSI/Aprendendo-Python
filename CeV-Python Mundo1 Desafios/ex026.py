# DESAFIO 026
# Faça um programa que leia uma frase pelo teclado e mostre
# a) Quantas vezes aparece a letra 'A'
# b) Em que posição aparece pela primeira vez
# c) Em que posição aparece pela última vez

frase = str(input('Digite o que quiser: ')).upper().strip()
print('a) Quantas vezes aparece a letra A          : {}'.format(frase.count('A')))
print('b) Em que posição aparece pela primeira vez : {}'.format(frase.find('A')+1))
print('c) Em que posição aparece pela última vez   : {}'.format(frase.rfind('A')+1))
