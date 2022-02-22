# Exercício 036: Aprovando Empréstimo
# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule a prestação mensal sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Salário do comprador? R$ '))
qtd_anos = int(input('Em quantos anos o empréstimo será pago? '))

valorParcela = valorCasa/(qtd_anos*12)
print('Valor da parcela: R$ {:.2f}'.format(valorParcela))
print('30% do salário  : R$ {:.2f}'.format(salario*0.30))

if valorParcela >= salario*0.30:
    print('Crédito não aprovado! ')
else:
    print('Crédito Aprovado! ')
