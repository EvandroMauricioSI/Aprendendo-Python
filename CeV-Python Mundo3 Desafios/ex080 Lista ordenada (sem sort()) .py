# Exercício 080: Lista ordenada (sem usar sort( ))
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
maior = menor = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:     # não tiver nenhum número na lista ou se n for maior que o último número da lista
        lista.append(n)
        print('add no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'add na posição {pos} da lista...')
                break
            pos += 1

print('\033[1m… '*27, '\033[m')

print(f'Os valores digitados em ordem foram: {lista}')
print('\033[1m… '*27, '\033[m')