from random import randint
n = randint(0, 10)
s = 0
e =  11
while not e == n:
    e = int(input('Escolha um numero de 0 a 10:  '))
    s += 1
print('Você precisou de {} tentativas para acertar'.format(s))