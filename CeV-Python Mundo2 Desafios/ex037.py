# Escreva um programa que leia um número inteiro qualquer e peça para o usuário qual será a base de conversão:
# 1 - para binário; 2 - para octal; 3 - para hexadecimal

valorInt = int(input('Informe um valo inteiro: '))
op = int(input('Para qual base quer converter: \n(1) BINÁRIO  (2)OCTAL  (3)HEXADECIMAL\n:: '))
if op == 1:
    print('{} em BINÁRIO = {}'.format(valorInt, bin(valorInt)))
elif op == 2:
    print('{} em OCTAL = {}'.format(valorInt, oct(valorInt)))
elif op == 3:
    print('{} em HEXADECIMAL = {}'.format(valorInt, hex(valorInt)))
else:
    print('Opão inválida! ')