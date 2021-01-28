# range(começa, termina, passo)
for c in range(0, 10):
    print(f'{c}')

for c in range(10, -1, -1):
    print(c)

# While com True roda infinitamente até fazer a condição de parada
while True '''condição''':
    '''codígo'''

    if n == 999:
        break  '''-> condição de parada'''

# Forma para deixar um decimal com quantidade de casas decimais que você quer
n = 2.34556
print(f'{n:.2f}')

# Formatação de como colocar as variáveis
# print(f'{nome:-^20}')   ===   print(f'{nome:(oqVaiColocarnessesLocais)(ondeVaiAdicionar)(Quantos)}')
# ondeVaiAdicionar ->  
# ^ -> centraliza
# < -> depois
# > -> antes



# .strip() -> tira espaços desnecessário no começo e no final
# .upper()  -> Transforma todas as letras em maiusculas
# .slit() -> separa as palavras transformando em uma lista
# 'coloca isso'.join() -> No meio da palavras separadas
frase = str(input('digite uma frase -> ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')