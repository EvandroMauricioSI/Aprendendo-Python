# Exercício 065: Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores

media = 0.0
cont = soma = maior = menor = 0
resp = 'S'
while resp == 'S':
    n = int(input('Digite um valor inteiro:  '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar digitando? [S/N]: ')).upper()
    if resp != 'S' and resp != 'N':
        print('Opção inválida')
        resp = str(input('Quer continuar digitando? [S/N]: ')).upper()
media = soma/cont
print('')
print('Foram digitados {} números e a médias entre eles foi {:.2f}'.format(cont, media))
print('Maior valor digitado foi {}'.format(maior))
print('Menor valor digitado foi {}'.format(menor))

