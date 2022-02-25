# Exercício 058: Jogo da Adivinhação
# Melhore o jogo do DESAFIO 028 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
computador = randint(1, 10)
print('- Computador: PENSEI NUM NÚMERO DE 0 a 10\nTente adivinhar o número que pensei')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? ": '))
    palpites += 1
    print('\033[0:33m', 'Processando...')
    sleep(0.6)
    if jogador == computador:
        print('\033[1:97:42m', ' Parabéns Você Acertou! ', '\033[m')
        acertou = True
    else:
        if jogador < computador:
            print('\033[1:34m','Mais...','\033[m', 'Tente mais uma vez:')
        elif jogador > computador:
            print('\033[1:31m','Menos...','\033[m', 'Tente mais uma vez:')
print('Número de tentativas = {}'.format(palpites))
