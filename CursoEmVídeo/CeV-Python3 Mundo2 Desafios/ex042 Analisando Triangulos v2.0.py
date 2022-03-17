# Exercício 042: Analisando Triângulos v2.0
# Refaço o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - escaleno: todos os lados diferente

print('-=-'*10)
print('Analizador de triângulos: ')
print('-=-'*10)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento : '))
r3 = float(input('Terceiro Segmento: '))
print('-=-'*10)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados FORMAM um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo! ')