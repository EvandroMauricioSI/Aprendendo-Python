# Exercício 044: Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# -> à vista dinheiro/cheque: 10% de desconto; -> à vista no cartão: 5% de desconto
# -> em até 2x no cartão: preço normal; -> 3x ou mais no cartão: 20% de juros

preco = float(input('Valor do produto: '))
print('FORMAS DE PAGAMENTO: \n[0] à vista dinheiro/cheque\n[1] à vista cartão\n'
      '[2] 2x no cartão\n[2} 3x ou mais no cartão')
op = int(input('Qual forma de pagamento? '))
if op == 0:
    total = preco - (preco * 0.1)
elif op == 1:
    total = preco - (preco * 0.05)
elif op == 2:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif op == 3:
    total = preco + (preco * 0.2)
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
else:
    total = preco
    print('Opção INVÁLIDA DE PAGAMENTO! Tente novamente! ')
print('Sua compra de R${:.2f} custará = R${:.2f}'.format(preco, total))

