# Fazer uma função para progressão aritimética
from time import sleep

def progressao_aritmetica(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'A contagem começa em {inicio} e termina em {fim} contando de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        while inicio <= fim:
            sleep(0.5)
            print(f'{inicio} -> ', end='', flush=True)
            inicio += passo
        print()
    else:
        while inicio <= fim:
            sleep(0.5)
            print(f'{inicio} -> ', end='', flush=True)
            inicio -= passo
        print()

# Programa Principal
progressao_aritmetica(1, 10, 1)
