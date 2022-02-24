# Exercício 058: Melhore o jogo do DESAFIO 028 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
computador = randint(1, 10)
print("- Computador: PENSEI NUM NÚMERO DE 0 a 10")
jogador = int(input('Tente adivinhar o número que o computador "pensou": '))
print('Processando...')
sleep(1)
contador = 1
while jogador != computador:
    print('Errou!')
    jogador = int(input('Tente adivinhar o número que o computador "pensou": '))
    contador += 1
print('Parabéns Você Acertou!')
print('Número de tentativas = {}'.format(contador))
