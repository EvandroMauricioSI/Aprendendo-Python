# Exercício 98 — Função de Contador.
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# (a) de 1 até 10, de 1 em 1; (b) de 10 até 0, de 2 em 2; (c) uma contagem personalizada

from time import sleep

def contagem(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('---------------------------------------------------')
    print(f'Contar de {início} até {fim} de {passo} em {passo}')
    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')


contagem(1, 10, 1)
sleep(2)
contagem(10, 0, 2)
sleep(2)
print('---------------------------------------------------')
print('Agora é sua vez de personalizar a contagem!')
começo = int(input('Início : '))
final = int(input('Fim    : '))
passo = int(input('Passo  : '))
contagem(começo,final, passo)
print('---------------------------------------------------')
