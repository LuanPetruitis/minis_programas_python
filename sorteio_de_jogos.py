from random import randint
from time import sleep
lista = []
jogos = []
print('-='*30)
print('     Joga na Mega Sena     ')
print('-='*30)
quant = int(input('Quantos jogos você quer fazer?  '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(2)
print('-='*5, 'Boa sorte', '-='*5)
