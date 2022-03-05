# DESAFIO 029
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que le foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite.

velocidade = int(input('Velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado! ')
    multa = (velocidade - 80) * 7.00
    print('O valor da multa é {:.2f}'.format(multa))
else:
    print('Velocidade dentro do limite permitido! ')
