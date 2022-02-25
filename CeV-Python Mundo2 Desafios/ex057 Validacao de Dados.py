# Exemplo 057: Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
#while sexo not in 'MmFf'
    sexo = str(input('Dados inválido! Por favor informe seu sexo [M/F]: ')).upper()
if sexo == 'M':
    print('Sexo {} MASCULINO {} registrado com sucesso'.format('\033[1:97:104m', '\033[m'))
else:
    print('Sexo {} FEMININO {} registrado com sucesso'.format('\033[1:97:105m', '\033[m'))
