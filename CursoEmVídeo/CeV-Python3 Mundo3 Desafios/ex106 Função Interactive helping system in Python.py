# Exercício 106 — Interactive helping system in Python:
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.

from time import sleep

cores = ('\033[m',  # 0 — sem cores
         '\033[0;30;41m',  # 1 — Vermelho
         '\033[0;30;42m',  # 2 — Verde
         '\033[0;30;43m',  # 3 — Amarelo
         '\033[0;30;44m',  # 4 — Azul
         '\033[0;30;45m',  # 5 — Roxo
         '\033[0;30;107m',  # 6 — Branco
         );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(1)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(0.5)


# MAIN
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!', 1)
