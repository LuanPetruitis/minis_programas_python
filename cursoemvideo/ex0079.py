v = []
r = 's'
while True:
    n = (int(input('Digite um valor: ')))
    if n not in v:
        v.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor não foi duplicado!')
    r = str(input('Você quer continuar [S/N]'))
    if r in 'Nn':
        break
print('A ordem dos valores é essa;')
v.sort()
print(v)