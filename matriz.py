matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = ma = sc = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: [{l}, {c}]    '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
    print()
print('=-'*30)
print(f'A soma dos valores pares é {sp}')
for l in range(0, 3):
    sc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {sc}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > ma:
        ma = matriz[1][c]
print(f'O maior valor da segunda linha é {ma}')