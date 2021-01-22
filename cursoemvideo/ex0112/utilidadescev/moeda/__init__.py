def aumentar(preço=0, taxa=0, formato=False):
    """

    :param preço: Preço normal
    :param taxa: Taxa que deseja aumentar o valor
    :return: Total do valor
    """
    resp = preço + (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preço=0, taxa=0, formato=False):
    """

    :param preço: Preço normal
    :param taxa: Taxa que deseja diminuir
    :return: Total do valor com a taxa
    """
    resp = preço - (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=False):
    """

    :param preço: Preço normal
    :return: Dobro do valor
    """
    resp  = preço * 2
    return resp if formato is False else moeda(resp)


def metade(preço=0, formato=False):
    """

    :param preço: Preço normal
    :return: Metade do valor
    """
    resp  = preço / 2
    return resp if not formato else moeda(resp)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, aument=0, red=0):
    """

    :param preço: Preço normal
    :param aument: Porcentagem de aumento
    :param red: Procentagem de redução
    :return: Todas as análises
    """
    print('='*30)
    print('       RESUMO DO VALOR')
    print('='*30)
    print(f'Preço análisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aument}% de aumento: \t{aumentar(preço, aument, True)}')
    print(f'{red}% de redução: \t{diminuir(preço, red, True)}')
    print('='*30)
