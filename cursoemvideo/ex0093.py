cadastro = {}
total_gols = []
cadastro['nome do jogador'] = str(input('Qual é o nome do jogador?  '))
tot = int(input(f'Quantas partidas o {cadastro["nome do jogador"]} jogou? '))
for c in range(0, tot):
    total_gols.append(int(input(f'Quantos gols o {cadastro["nome do jogador"]} fez na partida {c + 1}:   ')))
cadastro['gols'] = total_gols[:]
cadastro['total'] = sum(total_gols)
print('-='*30)
print(cadastro)
print('-='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*30)
print(f'O jogador {cadastro["nome do jogador"]} jogou {tot} partidas')
for i, v in enumerate(cadastro["gols"]):
    print(f'Na {i + 1}º partida ele fez {v} gols')