# Exercício 079: Valores únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valor = list()
print('{:-^40}'.format(' INÍCIO '))
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
    if op != 'S':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
valor.sort()
print('{:-^40}'.format(' FIM '))
print(f'Você digitou os valores {valor}')