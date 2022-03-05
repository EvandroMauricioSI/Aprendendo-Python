# Exercício Python 72: Número por extenso
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito','nove',
           'dez','onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove','vinte')
while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
print(f'Você digitou {extenso[n].upper()}')