# DESAFIO 007
# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

n1 = float(input('Informe a primeirna nota: '))
n2 = float(input('Informe a segunda nota  : '))
media = (n1+n2)/2
print('Média entre {:.1f} e {:.1f} = {:.1f}'.format(n1, n2, media))
