# Exercício 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1 = 120

n = int(input('Informe um valor para calcular seu fatorial: '))
fat = 0
cont = 0
while cont < n:
    fat = fat + (n * n-1)
    cont +=1
    print(fat)
