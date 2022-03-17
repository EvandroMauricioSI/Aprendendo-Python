# Exercício 073: Tuplas com Times de Futebol.
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre: (a) Os 5 primeiros times. (b) Os últimos 4 colocados.
# (c) Times em ordem alfabética. (d) Em que posição está o time da Chapecoense.

tabelaBr2018 = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
                'Atlético-MG', 'Athelico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
                'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
                'Sport', 'América-MG', 'Vitória', 'Vasco', 'Paraná')
for i in range(0, 20):
    print('{:^2} {}'.format(i + 1, tabelaBr2018[i]))
print('-' * 100)
print('(a) Mostre apenas os 5 primeiros colocados: ')
print('\033[1:34m', tabelaBr2018[0:5], '\033[m')
print('-' * 100)
print('(b) Mostre os 4 últimos colocados: ')
print('\033[1:31m', tabelaBr2018[-4:], '\033[m')
print('-' * 100)
print('(c) Uma lista em ordem alfabética: ')
print(sorted(tabelaBr2018))
print('-' * 100)
print('(d) Em que posição da tabela está o time Chapecoense: ')
for i in range(0, 20):
    if tabelaBr2018[i] == 'Chapecoense':
        print(f'O time está {i + 1}° na tabela ')
print('-' * 100)
print('FIM')
