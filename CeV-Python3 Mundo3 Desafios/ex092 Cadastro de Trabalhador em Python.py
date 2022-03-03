# Exercício 92 – Cadastro de Trabalhador em Python.
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()
dados['nome'] = str(input('NOME: '))
dados['nascimento'] = int(input('ANO NASCIMENTO: '))
dados['idade'] = (datetime.now().year - dados['nascimento'])
dados['ctps'] = int(input('N° DA CTPS (0 SE NÃO TIVER): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['salário'] = float(input('SALÁRIO: R$  '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('…'*30)
for chave, valor in dados.items():
    print(f'{(chave).upper() :.<20} : {valor}')
print('…'*30)
