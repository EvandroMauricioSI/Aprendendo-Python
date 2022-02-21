# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela a mensagem:
# -O primeiro valor é maior; -O segundo valor é maior ou -O não existe valor maior, os dois são iguais

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    print('O primeiro valor é maior')
elif x < y:
    print('O segundo valor é maior')
else:
    print('O não existe valor maior, os dois são iguais! ')