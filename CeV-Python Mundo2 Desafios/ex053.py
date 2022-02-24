# Exercício 053: Detector de Palíndromo
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
#  APOS A SOPA
#  A SACADA DA CASA
#  A TORRE DA DERROTA
#  O LOBO AMA O BOLO
#  ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
#inverso = junto[::-1] --> sem usar o ciclo for
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase informada É UM PALÍNDROMO')
else:
    print('A frase informada NÃO É UM PALÍNDROMO')

