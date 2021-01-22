aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['media'] >= 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
