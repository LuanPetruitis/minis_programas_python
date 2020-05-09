from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o nome -> '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida\033[m')
    sleep(1)

