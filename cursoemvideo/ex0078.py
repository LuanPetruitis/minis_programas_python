val = []
ma = 0
me = 0
for cont in range(0, 5):
    val.append(int(input(f'Digite {cont + 1}ª valor inteiro:  ')))
    if cont == 0:
        ma = me = val[cont]
    else:
        if val[cont] > ma:
            ma = val[cont]
        if val[cont] < me:
            me = val[cont]
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {ma} na posição  ', end='')
for i, v in enumerate(val):
    if v == ma:
        print(f'...{i + 1}', end='')
print()
print(f'O menor valor digitado foi {me} na posição  ', end='')
for i, v in enumerate(val):
    if v == me:
        print(f'...{i + 1}', end='')
