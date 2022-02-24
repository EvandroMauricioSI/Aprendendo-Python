# Exercício 045:
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
op = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada: '))

print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PÔ!!!\n')

if computador == 0: 
    if jogador == 0: 
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

print('-=-'*10)
print('Computador jogou:  {}'.format(op[computador]))
print('Jogador escolheu:  {}'.format(op[jogador]))
print('-=-'*10)


