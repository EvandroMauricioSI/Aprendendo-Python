def metade(n=0):
    return n/2

def dobro(n=0):
    return n*2

def aumentar(preço=0, porcentagem=0):
    aumento = preço * porcentagem / 100
    return preço + aumento

def diminuir(preço=0, porcentagem=0):
    redução = preço * porcentagem / 100
    return preço - redução

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
