# Exercício 93 – Cadastro de Jogador de Futebol.
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('NOME DO JOGADOR: '))
numPartidas = int(input('PARTIDAS JOGADAS: '))
for c in range(0, numPartidas):
    partidas.append((int(input(f'Quantos gols {(jogador["nome"]).upper()} fez na {c+1}ª partida: '))))
jogador['gols'] = partidas [:]
jogador['total'] = sum(partidas)
print('…'*50)
print(jogador)
print('…'*50)
for chave, valor in jogador.items():
    print(f'{(chave).upper() :.<20}  {valor}')
print('…'*50)
print(f'O jogador {jogador["nome"]} jogou {numPartidas} partidas')
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas') # também funciona
for índice, valor in enumerate(jogador["gols"]):
    print(f'Na {índice+1}ª partida fez {valor} gols')
print(f'Foi um total de {jogador["total"]} gols')