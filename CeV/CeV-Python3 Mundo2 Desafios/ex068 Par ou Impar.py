# Exercício 069: Par ou Impar
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final no jogo

from random import randint
vitórias = 0
print('-=-'*10)
print('Vamos jocar Par ou Impar?')
print('-=-'*10)
while True:
    jogador = int(input('Digite um valor: '))
    maquina = randint(0, 10)
    total = maquina + jogador
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if op == 'P':
        if total%2 == 0:
            print('Deu PAR')
            print('VOCÊ GANHOU!')
            vitórias += 1
        else:
            print('Deu ÍMPAR')
            print('COMPUTADOR GANHOU!')
            break
    if op == 'I':
        if total%2 == 0:
            print('Deu PAR')
            print('COMPUTADOR GANHOU! ')
            break
        else:
            print('Deu IMPAR')
            print('VOCÊ GANHOU!')
            vitórias += 1

print('GAME OVER! ')
print('-=-'*10)
print(f'Você Venceu {vitórias}x')
