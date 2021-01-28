print('-='*20)
print('BANCO DEV')
print('-='*20)
valor = int(input('Quanto você quer sacar: '))
total = valor
cinquenta = vinte = dez = dois = um = 0
while True:
    if total >= 50:
        total -= 50
        cinquenta += 1
    elif total >= 20:
        total -= 20
        vinte += 1
    elif total >= 10: 
        total -= 10
        dez += 1
    elif total >= 2:
        total -= 2
        dois += 1
    elif total == 1:
        total -= 1
        um += 1
    else: 
        break
print('-'*30)
print('Você vai receber: ')
print(f'Notas de 50: {cinquenta}')
print(f'Notas de 20: {vinte}')
print(f'Notas de 10: {dez}')
print(f'Notas de 2: {dois}')
print(f'Notas de 1: {um}')
