# Exercício 105 — Analisando e gerando Dicionários:
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# Quantidade de notas; A maior nota; A menor nota; A média da turma; A situação (opcional)
# Adicione também as docstrigs.

def notas(*n, sit=False):
    """
    -=-=- Função para analizar notas e situação do aluno -=-=-
    :param n: notas da turmo (uma ou mais notas).
    :param sit: valor opcional exibir ou não a situação da turma.
    :return: dicionário com várias informações da turma (total de notas, maior nota, menor nota, média, situação).
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa Principal (MAIN)
resp = notas(5.5, 2.5, 3, 8.5, 10, 4.3)
print(resp)
print('-' * 70)
help(notas)
print('-' * 70)
