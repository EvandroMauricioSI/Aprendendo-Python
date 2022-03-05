# Exercício 95 – Aprimorando os Dicionários.
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
from typing import Union, List

time = list()
jogador = dict()
partidas = list()
while True:
    # ler dados dos jogares
    jogador.clear()
    jogador['nome'] = str(input('NOME DO JOGADOR: '))
    numPartidas = int(input('PARTIDAS JOGADAS: '))

    partidas.clear()
    for c in range(0, numPartidas):
        partidas.append((int(input(f'Quantos gols {(jogador["nome"]).upper()} fez na {c+1}ª partida: '))))
    jogador['gols'] = partidas [:]
    jogador['total'] = 0
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) # como jogador é um dicionário usamos .copy()

    while True: # validando resposta se quer ou não continuar
        resp = str(input('Quer continuar [S/N]?: ')).upper()[0]
        if resp in 'SN': # para verificar se escolheu umra opção válida
            break
        print('ERRO! Digite apenas S ou N') #else implícito
    if resp in 'Nn':
        break

print('…'*50)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('…'*50)
for k, v in enumerate(time):
    print(f'{k:>3}', end='  ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('…'*50)
while True:
    busca = int(input('Buscar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador com cód {busca}')
    else:
        print(f'-------LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}--------')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo{i+1} fez {g} gols')
        print('…' * 50)
print(' VOLTE SEMPRE! ')
