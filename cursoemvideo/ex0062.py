print('Gerador de PA')
print('-='*10)
p = int(input('Primeiro termo:  '))
razão = int(input('Razão da PA:  '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print(' PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')