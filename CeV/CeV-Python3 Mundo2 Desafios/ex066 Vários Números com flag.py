# Exercício 066: Vários Números com flag
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')