# Exercício 081: Extraindo dados de uma Lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break

valores.sort(reverse=True)
print('… '*30)
print(f'(a) quantos números foram digitados? \n   R.: Você digitou {len(valores)} elementos')
print(f'(b) a lista de valores, ordenada de ordem decrescente:\n   {valores} ')
print('(c) se o valor 5 foi digitado e está ou não na lista?')
if 5 in valores:
    print('   R.: \033[1:32m \033[7m SIM \033[m \033[1:32m, o número 5 está na lista\033[m')
else:
    print('   R.: \033[1:31m \033[7m NÃO \033[m \033[1:31m, o número 5 não está na lista\033[m')
print('… '*30)