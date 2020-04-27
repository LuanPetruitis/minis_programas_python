def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opicional) mostrar ou não a conta
    :return: Mostrar o reultado
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)