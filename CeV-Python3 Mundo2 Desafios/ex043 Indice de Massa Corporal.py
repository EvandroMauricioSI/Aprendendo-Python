# Exercício 043: Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# -> Abaixo de 18,5: Abaixo do Peso
# –> Entre 18,5 e 25: Peso Ideal
# –> 25 até 30: Sobrepeso
# –> 30 até 40: Obesidade
# –> Acima de 40: Obesidade Mórbida

altura = float(input('Qual sua altura (em metros): '))
peso = float(input('Qual o seu peso (em quilos): '))
imc = peso / (altura**2)
print('Seu IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA, CUIDADO! ')

