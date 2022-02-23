# Exercício 051: 
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Primeiro termo PA: '))
r = int(input('Razão da PA:       '))
print(t)
for i in range(0, 9):
    x = t * r
    t = x
    print(x)

