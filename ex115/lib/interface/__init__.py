def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for items in lista:
        print(f'\033[33m{c}\033[m -\033[34m {items}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m  ')
    return opc
