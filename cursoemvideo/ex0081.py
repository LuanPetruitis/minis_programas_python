n = []
cont = 0
while True:
    n.append(int(input('Digite um valor: ')))
    cont += 1
    r = input('Quer continuar [S/N]?  ')
    if r in 'Nn':
        break
n.sort(reverse=True)
print('='*50)
print(f'Você digitou {cont} números')
print(f'A ordem decrescente é -> {n}')
if 5 in n:
    print('Sua lista tem o valor 5')
else:
    print('Sua lista não tem o valor 5')