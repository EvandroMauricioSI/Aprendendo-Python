# DESAFIO 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários maiores que R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)  # outra forma de calcular porcentagem
else:
    novo = salario + (salario * 0.10)
print('Novo salário = R${:.2f}'.format(novo))
