import moeda

p = float(input('Digite o preço:    R$ '))
print(f'O dobro de R$ {p} é {moeda.dobro(p)}')
print(f'A metade de R$ {p} é {moeda.metade(p)}')
print(f'Aumentando o preço em 10% o valor {moeda.aumentar(p, 10)}')
print(f'Diminuindo o preço em 10% o valor {moeda.diminuir(p, 10)}')
