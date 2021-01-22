n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('os dois são iguais')
input("Precione enter para finalizar o programa")