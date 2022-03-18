# Exercício 107 — Exercitando módulos em Python:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex107 import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {p} = {moeda.metade(p)}')
print(f'O dobro de {p}  = {moeda.dobro(p)}')
print(f'Aumentando 10%  = {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%   = {moeda.diminuir(p, 13)}')