# Exercício 101 — Funções para votação
# Crie uma função que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        return (print(f'Com {idade} anos NÃO SE VOTA!'))
    elif 16 <= idade <18 or idade > 65:
        return (print(f'Com {idade} anos o voto é OPCIONAL!'))
    else:
        return (print(f'Com {idade} anos voto é OBRIGATÓRIO!'))

ano_nascimento = int(input('Infome o ano que  você nasceu: '))
voto(ano_nascimento)

