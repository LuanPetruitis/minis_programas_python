n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))
print(f'Você digitou os números {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
print(f'O valor três foi digitado na posição {n.index(3) + 1}')
cont = 0
for num in n:
    if num % 2 == 0:
        cont += 1
print(f'Você digitou {cont} numeros pares')