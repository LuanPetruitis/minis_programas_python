def aumentar(preço, taxa):
    """

    :param preço: Preço normal
    :param taxa: Taxa que deseja aumentar o valor
    :return: Total do valor
    """
    resp = preço + (preço * taxa/100)
    return resp


def diminuir(preço, taxa):
    """

    :param preço: Preço normal
    :param taxa: Taxa que deseja diminuir
    :return: Total do valor com a taxa
    """
    resp = preço - (preço * taxa/100)
    return resp


def dobro(preço):
    """

    :param preço: Preço normal
    :return: Dobro do valor
    """
    resp  = preço * 2
    return resp

def metade(preço):
    """

    :param preço: Preço normal
    :return: Metade do valor
    """
    resp  = preço / 2
    return resp
