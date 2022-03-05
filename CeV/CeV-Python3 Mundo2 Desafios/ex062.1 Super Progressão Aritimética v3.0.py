# Exercício 062: Super Progressão Aritmética v3.0
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

termos = 10
primeiro = int(input('Primeiro termo PA: '))
razão = int(input('Razão da PA:       '))
último = primeiro + (termos - 1) * razão


while termos != 0:
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
    termos = int(input('Quantos termos a mais gostaria de exibir? '))
    último = (primeiro+1) + (termos - 1) * razão

print('FIM')