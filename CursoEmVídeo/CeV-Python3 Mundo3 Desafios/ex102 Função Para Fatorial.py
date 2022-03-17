# Exercício 102 — Função para Fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=False):
    """
    || Função para calcular o fatorial de um número ||
    :param n: O Número a ser calculado
    :param show: (opcional). Se True mostra o passo a passo da conta
    :return: o valor do fatorial do número n
    """
    fat = n
    for c in range(n, 0, -1):
        fat *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat

print(fatorial(4, show=True))
help(fatorial)