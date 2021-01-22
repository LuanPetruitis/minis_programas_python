from ex0109 import moeda

p = float(input('Digite o preço:    R$ '))
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando o preço em 10% o valor {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo o preço em 10% o valor {moeda.diminuir(p, 10, True)}')
