# Exercício 040: Aquela Clássica da Média
# Crie um programa que leia duas notas de um alugo e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - média abaixo de 5.0: reprovado
# - média entre 5.0 e 6.9: recuperação
# - média 7.0 ou superior: aprovado

nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
media = (nota1+nota2)/2
print('Média = {:.1f}'.format(media))
if media<5.0:
    print('{} Reprovado! {}'.format('\033[1:97:41m', '\033[m' )) #pode-se usar \033 ou \33
elif (media >= 5.0) and (media < 7.0):
    print('{} Recuperação {}'.format( '\33[1:97:43m', '\33[m'))
else:
    print('\033[1:97:42m', 'Aprovado!', '\33[m') # sem usar o .format(...)
