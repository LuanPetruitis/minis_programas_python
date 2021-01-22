e = 0
while not e == 5:
    e = int(input('''Escolha O que deseja fazer;
    [1] soma
    [2] multiplicar
    [3] maior
    [4] Calcular o fatorial de um número
    [5] sair    
    '''))
    if e == 1:
        n1 = float(input('Digite um numero;  '))
        n2 = float(input('Digite outro numero;  '))
        s = n1 + n2
        print(s)
    elif e == 2:
        n1 = float(input('Digite um numero;  '))
        n2 = float(input('Digite outro numero;  '))
        m = n1 * n2
        print(m)
    elif e == 3:
        n1 = float(input('Digite um numero;  '))
        n2 = float(input('Digite outro numero;  '))
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif e == 4:
        n = int(input('Digite um numero inteiro;  '))
        f = n
        while not n == 1:
            f = f * (n - 1)
            n -= 1
        print(f)
