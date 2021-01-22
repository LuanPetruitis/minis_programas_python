cont = soma = 0
while True:
    n = int(input('digie um número inteiro:  (Para parar digite 999)'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores é {soma}')