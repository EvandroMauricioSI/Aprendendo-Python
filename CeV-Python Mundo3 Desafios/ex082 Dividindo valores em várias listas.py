# Exercício 082 – Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

num = list()
pares = list()
ímpares = list()

while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)

print(f'Todos os valores digitados ... : {num}')
print(f'Os valores pares ............. : {pares}')
print(f'Os valores ímpares ........... : {ímpares}')
