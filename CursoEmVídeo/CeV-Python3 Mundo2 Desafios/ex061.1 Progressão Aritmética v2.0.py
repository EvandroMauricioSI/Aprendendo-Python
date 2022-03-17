# Exercício 061: Progressão Aritimética v2.0
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo PA: '))
razão = int(input('Razão da PA:       '))
último = primeiro + (10 - 1) * razão

prox = 0
while primeiro != último:
    if prox == 0:
        print(primeiro, end=' -> ')
        prox = primeiro + razão
    else:
        prox = primeiro + razão
        primeiro = prox
        print(prox, end=' -> ')
print('FIM')