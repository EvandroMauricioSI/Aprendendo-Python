# Exercício 040: Aquela Clássica da Média
# Crie um programa que leia duas notas de um alugo e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - média abaixo de 5.0: reprovado
# - média entre 5.0 e 6.9: recuperação
# - média 7.0 ou superior: aprovado

nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
media = (nota1+nota2)/2
print('Nota 1 = {:.1f}, Nota 2 = {:.1f}, Média = {:.1f} logo '.format(nota1, nota2, media), end='')
if media<5.0:
    print('Reprovado!')
elif (media >= 5.0) and (media < 7.0):
    print('Recuperação')
else:
    print('Aprovado!')
