# Tuplas
# Tuplas são imutáveis  *********************
# pode ser sem parenteses
# Pode ler dados de tipos diferentes, como caracter, inteiro e etc...
nome_da_variavel = ('suco', 'Hamburguer', 'Pizza', 'Pudim')
print(nome_da_variavel)
print(nome_da_variavel[1])
print(nome_da_variavel[-2])
print(nome_da_variavel[1:3])
print(nome_da_variavel[2:])
print(nome_da_variavel[:3])

# Colocar em ordem
print(sorted(nome_da_variavel))


for c in nome_da_variavel:
    print(c)

# Para mostrar a posição
for pos, c in enumerate(nome_da_variavel):
    print(c)


# Lista
dados = list()
pessoas = list()
# pessoas = [['~~~~~', 25], ['~~~~~', 25], ['~~~~~', 25]]
dados.append('Luan')
dados.append('19')
pessoas.append(dados[:])
dados.clear()
dados.append('João')
dados.append('21')
# Faz copia sem o [:] coloca em todos os valores da lista
pessoas.append(dados[:])

print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[1])
print(pessoas)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')