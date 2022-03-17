# Exercício 96 – Função que calcula área.
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} é de {a} m2.')


print('CONTROLE DE TERRENOS')
print('--------------------')
largura = float(input('LARGURA (m)    : '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)