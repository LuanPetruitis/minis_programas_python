def área(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} X {comp} é de {a}m²')


#Programa principal
print('Controle de Terrenos')
print('-' * 30)
l = float(input('largura (m): '))
c = float(input('comprimento (m): '))
área(l, c)
