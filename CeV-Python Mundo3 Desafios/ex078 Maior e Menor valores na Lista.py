# Exercício 078: Maior e Menor valores na lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
cont = maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para o Posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
        posMaior = posMenor = c
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Você digitou os valores {valores}')
print(f'Maior valor digitado foi {maior} na(s) posição(ões): ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end=' ')
print()
print(f'Menor valor digitado foi {menor} na(s) posição(ões): ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end=' ')
print()