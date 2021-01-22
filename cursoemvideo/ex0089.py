ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 +n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar [S/N]?   '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Nota 1":^8}{"Nota 2":^8}{"Média":>8}')
print('-'*40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[1][0]:^8}{a[1][1]:^8}{a[2]:>8.1f}')