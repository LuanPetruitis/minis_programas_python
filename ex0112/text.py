from ex0112.utilidadescev import moeda
from ex0112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço:    R$ ')
aumento = int(input('Porcentagem de aumento: '))
reducao = int(input('Porcentagem de redução: '))
moeda.resumo(p, aumento, reducao)
