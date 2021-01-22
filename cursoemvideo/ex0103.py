def ficha(nome='<desconhecido>', gols=0):
    print('-'*40)
    print(f'O jogador {nome}, marcou {gols} gols')


# Programa Principal
n = str(input('Qual é o nome do jogador:  '))
g = str(input(f'Quantos gols o jogador {n} marcou:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
