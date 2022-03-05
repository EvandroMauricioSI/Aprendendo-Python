# Exercício 068: Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor? : '))
    print('-' * 40)
    if n < 0:
        break
    for i in range(0, 11):
        print(f'{i:<4} X {n:4}  =  {i*n:<4}')
print('Programa de Tabuada Encerrado!')

