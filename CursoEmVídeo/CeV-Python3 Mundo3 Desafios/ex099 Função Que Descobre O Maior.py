# Exercício 99 — Função que descobre o maior.
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* núm):
    print('-'*40)
    print('Analisando os valores passados...')
    cont = maiorNum = 0
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maiorNum = valor
        else:
            if valor > maiorNum:
                maiorNum = valor
        cont += 1
    print(f'Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor foi {maiorNum}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(2, 1)
maior(6)
maior()

