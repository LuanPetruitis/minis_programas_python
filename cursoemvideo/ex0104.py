def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Você não digitou um número tente novamente\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')