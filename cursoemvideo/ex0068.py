print('=-'*20)
print('Vamos jogar par ou impar')
print('=-'*20)
from random import randint
cont = 0
while True:
    tipo = str(input('Você escolhe par ou impar? [P/I]')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu! ')
            cont +=1
        else:
            print('Você Perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu! ')
            cont += 1
        else:
            print('Você Perdeu! ')
            break
print(f'Você ganhou {cont} vezes ')