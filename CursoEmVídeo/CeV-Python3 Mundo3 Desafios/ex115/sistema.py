from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

#if arquivoExiste(arq):
#    print('Arquivo encontrado com sucesso')
#else:
#    print('Arquivo não encontrado')
#    criarArquivo(arq)

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])
    if resposta == 1:   # Opção de listar conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:     # Opção para adicionar dados
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[36mSaindo do Sistema! Até Logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')



