ano = int(input('Digite o ano que você nasceu: '))
idade =  2021 - ano
if idade == 18:
    print('Esta no ano de você se alistar')
elif idade > 18:
    p =  idade - 18
    print('Já passou {} dois anos que você tinha que ter se alistado'.format(p))
else:
    f = 18 - idade
    print('Não esta no ano de você se alistar ainda falta {} anos'.format(f))