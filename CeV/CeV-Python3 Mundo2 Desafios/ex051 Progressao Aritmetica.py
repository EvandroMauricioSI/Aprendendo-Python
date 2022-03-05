# Exercício 051: Progressão Aritmética
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo PA: '))
razão = int(input('Razão da PA:       '))
último = primeiro + (10 - 1) * razão
for c in range(primeiro, último + razão, razão):
    print(c, end=' -> ')
print('FIM')



