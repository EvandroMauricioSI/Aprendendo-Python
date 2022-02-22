# Exercício 037: Conversor de Bases Numéricas
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário qual será a base de conversão:
# 1 - para binário; 2 - para octal; 3 - para hexadecimal

valorInt = int(input('Informe um valo inteiro: '))
op = int(input('Para qual base quer converter: \n(1) BINÁRIO  (2)OCTAL  (3)HEXADECIMAL\n:: '))
if op == 1:
    print('{} em BINÁRIO = {}'.format(valorInt, bin(valorInt)[2:]))
elif op == 2:
    print('{} em OCTAL = {}'.format(valorInt, oct(valorInt)[2:]))
elif op == 3:
    print('{} em HEXADECIMAL = {}'.format(valorInt, hex(valorInt)[2:]))
else:
    print('Opção inválida! ')