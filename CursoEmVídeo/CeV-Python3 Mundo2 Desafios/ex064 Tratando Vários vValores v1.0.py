# Exercício 064: Tratando vários valores v1.0
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = 0
contador = 0
n = 1
while n != 999:
    n = int(input('Digite um valor qualquer  ou 999 para sair]: '))
    if n == 0:
        soma = soma
        contador = contador
    else:
        soma += n
        contador += 1
print('Foram digitados {} valores e a soma deles é igual a {}'.format(contador, soma))