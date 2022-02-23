# Exercício 048:
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0
for c in range(0, 500):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos números múltiplos de 3 no intervalo de 0 a 500 = {}'.format(soma))
