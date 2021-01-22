galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('NOME:'))
    while True:
        pessoa['sexo'] = str(input('Qual e o sexo [M/F]?  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite M para masculino e F para feminino')
    pessoa['idade'] = int(input('Qual e a  idade? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja qcontinuar [S/N]?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'A-) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B-) A média de idade é de {media:5.2f} anos')
print('C-) Mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print()
print('D-) Lista das pessoas que estão com a idade acima da média', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<<<ENCERRADO>>>')