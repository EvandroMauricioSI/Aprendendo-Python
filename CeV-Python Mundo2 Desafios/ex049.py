# Exercício 049
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, sendo que agora,
# utilizando o laço for.

num = int(input('número: '))
for c in range(0, 11):
    print('{:3}   + {:3} = {:3}'.format(c, num, c+num))