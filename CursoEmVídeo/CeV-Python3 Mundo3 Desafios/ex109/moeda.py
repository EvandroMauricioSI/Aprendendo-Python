def metade(preço=0, formato=False):
    resultado = preço / 2
    return resultado if formato is False else moeda(preço)

def dobro(preço=0, formato=False):
    resultado = preço * 2
    return resultado if formato is False else moeda(preço)

def aumentar(preço=0, porcentagem=0, formato=False):
    resultado = preço + (preço * porcentagem / 100)
    return resultado if formato is False else moeda(preço)

def diminuir(preço=0, porcentagem=0, formato=False):
    resultado = preço - (preço * porcentagem / 100)
    return resultado if formato is False else moeda(preço)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
