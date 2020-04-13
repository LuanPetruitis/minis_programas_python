pessoas = []
d = []
ma = me = 0
while True:
    d.append(input('Qual é o nome? '))
    d.append(input('Qual é o peso ? '))
    if len(pessoas) == 0:
        ma = me = d[1]
    else:
        if d[1] > ma:
            ma = d[1]
        if d[1] < me:
            me = d[1]
    pessoas.append(d[:])
    r = str(input('Quer continuar [S/N]? '))
    d.clear()
    if r in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {pessoas}')
print(f'Ao todo vôce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {ma} Kg,  o nome das pessoas são, ', end='')
for p in pessoas:
    if p[1] == ma:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso foi de {me} Kg, o nome delas são, ', end='')
for n in pessoas:
    if n[1] == me:
        print(f'{n[0]}, ', end='')