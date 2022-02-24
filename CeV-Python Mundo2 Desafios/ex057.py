# Exemplo 057:
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Opção inválida, tente novamente! ')
    sexo = str(input('Informe o sexo da pessoa [M/F]: ')).upper()
print('FIM')