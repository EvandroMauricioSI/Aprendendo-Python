# Exercício 103 — Ficha do Jogador:
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s)')

n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols feito: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
