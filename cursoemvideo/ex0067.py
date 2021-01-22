cont = 0
while True:
    print('-' * 40)
    t = int(input('Você quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if t < 0:
        break
    for cont in range(0,11):
        m = cont * t
        print(f'{t} * {cont} = {m}')
        cont += 1