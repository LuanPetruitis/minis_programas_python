soma = 0
cont = 0
for c in range(1, 50, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} elementos é {}'.format(cont, soma))