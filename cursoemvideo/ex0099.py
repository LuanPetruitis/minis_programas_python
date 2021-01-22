from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados! ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
            cont += 1
    print(f'Foi informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')



#Programa Principal
maior(2, 9, 3, 4, 5, 1)
maior(3, 2, 1, 6)
maior(1, 2)
maior(6)
maior()