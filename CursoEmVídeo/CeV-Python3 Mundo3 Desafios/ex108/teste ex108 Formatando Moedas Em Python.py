# Exercício 108 — Formatando Moedas em Python:
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
# os números como um valor monetário formatado.

from ex108 import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} = {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)}  = {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%  = {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%   = {moeda.moeda(moeda.diminuir(p, 13))}')