# Exercício 109 — Formatando Moedas Em Python:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from ex109 import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} = {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)}  = {moeda.dobro(p, True)}')
print(f'Aumentando 10%  = {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%   = {moeda.diminuir(p, 13, True)}')