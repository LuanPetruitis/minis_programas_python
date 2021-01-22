n1 = float(input('Digite o primeiro segmento'))
n2 = float(input('Digite o segundo segmento'))
n3 = float(input('Digite o terceiro segmento'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima formam um triangulo')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÔCELES')
else:
    print('Os segmentos acima não formam um triangulo')
input("Precione enter para finalizar o programa")
