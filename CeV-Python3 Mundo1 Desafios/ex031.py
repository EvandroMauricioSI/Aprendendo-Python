# DESAFIO 031
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por cada km para viagens até 200km
# e R$0,45 para viagens mais longas.

distancia: float = float(input('Distancia da viagem em km: '))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print('O valor da passagem é R${:.2f}'.format(preço))
