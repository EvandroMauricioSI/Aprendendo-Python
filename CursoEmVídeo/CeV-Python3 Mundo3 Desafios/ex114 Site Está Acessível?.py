# Exercício 114 — Site está acessível?

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO Site Pudim Não Está Acessível Neste Momento!\033[m')
else:
    print('\033[32mConsegui Acessar O Site Pudim Com Sucesso!\033[m')
    # print(site.read())  mostra o conteúdo html do site