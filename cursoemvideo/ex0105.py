def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação dos alunos.
    :param n: uma ou mais notas dos aulunos (aceita varias)
    :param sit: valor opicional indicando se deve ou não adcionar a situação
    :return: dicionário com varias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(10, 9, 5, 7, sit=True)
print(resp)
help(notas)