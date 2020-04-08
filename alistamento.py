a = int(input('digite o ano que você nasceu: '))
h =  2020 - a
if h == 18:
    print('Esta no ano de você se alistar')
elif h > 18:
    p = h - 18
    print('Já passou {} dois anos que você tinha que ter se alistado'.format(p))
else:
    f = 18 - h
    print('Não esta no ano de você se alistar ainda falta {} anos'.format(f))