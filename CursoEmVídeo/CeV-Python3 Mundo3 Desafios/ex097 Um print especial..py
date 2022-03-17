# Exercício 97 – Um print especial.
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Olá, Mundo!')
escreva('Evandro Narciso Mauricio')
escreva('CeV')