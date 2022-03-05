# DESAFIO 028
# Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(1, 5)
print("- Computador: PENSEI NUM NÚMERO DE 0 a 5")
jogador = int(input('Tente adivinhar o número que o computador "pensou": '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('Você VENCEU')
else:
    print('Você PERDEU! o computador escolheu {}!'.format(computador))
