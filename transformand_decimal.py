while True:
    print('''Escolha uma dessas opções para conversão
        [1] BINÁRIO
        [2] OCTAl
        [3] HEXADECIMAL
        [4] SAIR DO PROGRAMA''')
    o = int(input('qual é a sua opção: '))
    if o == 4:
        print('Até breve!')
        break
    else:
        n = int(input('digite um numero inteiro: '))
        if o == 1:
            print(f'\033[0;33m{n} convertido para binário é {bin(n)[2:]}\033[m')
        if o == 2:
            print(f'\033[0;33m{n} convertido para octal é {oct(n)[2:]}\033[m')
        if o == 3:
            print(f'\033[0;33m{n} convertido para hexadecimal é {hex(n)[2:]}\033[m')
        if o > 4:
            print('Opção inválida!')
