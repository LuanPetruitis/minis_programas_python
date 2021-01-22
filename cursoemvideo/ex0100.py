from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f' {n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar():
    soma = 0
    for v in número:
        if v %  2 == 0:
            soma += v
    print(soma)

número = list()
sorteia(número)
print(número, end='')
print('. A soma dos números pares vale ', end='')
somapar()