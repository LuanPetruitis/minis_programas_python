from ex0108 import moeda

p = float(input('Digite o preço:    R$ '))
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando o preço em 10% o valor {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo o preço em 10% o valor {moeda.moeda(moeda.diminuir(p, 10))}')
