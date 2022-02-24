# Exemplo 047: Contagem de pares
# Crie um programa que mostre tela todos os números pares que estão no intervalo entre 1 e 50.

print('for i in range (1,51, 1): ')
for c in range(1, 51):
   if c % 2 == 0:
       print(c, end=' ')
print('Acabou!')

print('\nfor i in range (2,51, 2): ')
for i in range(2, 51, 2):
    print(i, end=' ')
print('Acabou!')