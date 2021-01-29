# def nomeFuncao(qualquerTipo):
# qualquer tipo, podendo ser listas, inteiros e etc...
#     ...

def nomeFuncao(msg):
    '''
        Aqui você pode fazer sua DOCSTRINGS
        e explicar o que sua função faz
    '''
    
    print('-'*50)
    print(msg)
    print('-'*50)

# * é para desempacotar, isso permite que você passa quantos parametros quiser para função

def contador(* num):
    for valor in num:
        print(f'{valor}',end='')
    print('FIM')


# Minimo 2 linhas vazias, para separar
# Programa principal

nomeFuncao("CURSO EM VIDEO")
nomeFuncao("SISTEMA DE ALUNOS")
nomeFuncao("SISTEMA DE PROFESSORES")

contador(2, 3, 4)
contador(2, 3, 4, 4)
contador(2, 3, 4, 7, 4)

# ############################################
# Interactive help
# Explica a função
# help(print)
# help(nomeFuncao)
