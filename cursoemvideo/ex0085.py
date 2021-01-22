n = [[], []]
valor = 0
for cont in range(1, 8):
    valor = int(input('Digite o  valor:'))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort()
print(f'Os valores pares são {n[0]}')
print(f'Os valores ímpares são {n[1]}')