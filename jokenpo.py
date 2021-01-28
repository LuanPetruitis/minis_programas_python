from random import randint
itens = ('pedra', 'papel', 'tesoura')
c = randint(0, 2)
print('''[0] pedra
[1] papel
[2] tesoura
----------------
JO
KEN
PO!
----------------''')
v = int(input('qual numero voce escolhe:  '))
print('-='*10)
print('O computador escolheu {}'.format(itens[c]))
print('Você escolheu {}'.format(itens[v]))
print('-='*10)
if c == 0:
    if v == 0:
        print('Empatou!')
    elif v == 1:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif c == 1:
    if v == 0:
        print('Você perdeu!')
    elif v == 1:
        print('Empatou!')
    else:
        print('Você ganhou!')
elif c == 2:
    if v == 0:
        print('Você ganhou!')
    elif v == 1:
        print('Você perdeu!')
    else:
        print('Empatou!')
else:
    print('Você digitou um número que não existe!')