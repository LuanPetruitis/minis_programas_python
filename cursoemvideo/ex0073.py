times = ('corinthians', 'palmeiras', 'santos', 'gremio')
print(f'Esta é a lista de times do brasileirão: {times}')
print('-='*15)
print(f'Este são os dois primeiros times {times[0:2]}')
print('-='*15)
print(f'Este são os dois ultimos: {times[-2:]}')
print(f'Esta e a ordem alfabética deles {sorted(times)}')
print(f'O corinthians esta na {times.index("corinthians")+1} posição')