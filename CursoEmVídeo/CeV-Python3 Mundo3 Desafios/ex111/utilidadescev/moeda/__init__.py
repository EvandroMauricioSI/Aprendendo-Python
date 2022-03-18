def metade(preço=0, formato=False):
    resultado = preço / 2
    return resultado if formato is False else moeda(resultado)

def dobro(preço=0, formato=False):
    resultado = preço * 2
    return resultado if formato is False else moeda(resultado)

def aumentar(preço=0, porcentagem=0, formato=False):
    resultado = preço + (preço * porcentagem / 100)
    return resultado if formato is False else moeda(preço)

def diminuir(preço=0, porcentagem=0, formato=False):
    resultado = preço - (preço * porcentagem / 100)
    return resultado if formato is False else moeda(preço)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, aumento=10, redução=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:  \t{moeda(preço)}')
    print(f'Dobro do preço :  \t{dobro(preço, True)}')
    print(f'Metade do preço:  \t{metade(preço, True)}')
    print(f'{aumento}% de aumento :  \t{moeda(aumentar(preço, aumento))}')
    print(f'{redução}% de redução :  \t{moeda(diminuir(preço, redução))}')
    print('-' * 30)

