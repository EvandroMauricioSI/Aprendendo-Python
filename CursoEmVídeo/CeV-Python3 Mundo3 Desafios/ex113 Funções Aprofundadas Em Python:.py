# Exercício 113 — Funções aprofundadas em Python:
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma
# funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um valor INTEIRO VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! Entrada de Dados Interrompida Pelo Usuário!\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um valor INTEIRO VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! Entrada de Dados Interrompida Pelo Usuário!\033[m')
            return 0
        else:
            return n

num1 = leiaInt('Digite um Inteiro: ')
num2 = leiaFloat('Digite um Real   : ')
print(f'Valores digitados:  Inteiro {num1}; Real: {num2}')



