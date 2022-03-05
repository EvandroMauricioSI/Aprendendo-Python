# Exercício 083 – Validando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

expressão = str(input('Digite a expressão matemática: '))
pilha = []
for símb in expressão:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão VÁLIDA!')
else:
    print('Expressão INCORRETA!')