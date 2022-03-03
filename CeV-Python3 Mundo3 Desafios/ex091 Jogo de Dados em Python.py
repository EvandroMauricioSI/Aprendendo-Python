# Exercício 91 – Jogo de Dados em Python.
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)

#jogo = {'Jogador1': randint(1, 6),     |
#        'Jogador2': randint(1, 6),     | Também pode ser feito dessa forma
#        'Jogador3': randint(1, 6),     |
#       'Jogador4': randint(1, 6)}      |

for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)
print('…'*35)
print(f'{"RANK DOS JOGADORES":^35}')
print('…'*35)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for índice, valor in enumerate(ranking):
    print(f'{índice+1}° lugar: {valor[0]} com {valor[1]} pontos')
    sleep(1)
print('…'*35)