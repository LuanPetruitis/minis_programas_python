anos = int(input("Você quer fazer a média de quantos anos: "))
totalAnos = anos * 12
e = 0
soma = 0
while not e == totalAnos:
    e = e + 1
    n1 = float(input(f'Digite o {e}º mês em R$  '))
    soma = n1 + soma
media = soma / totalAnos
print(f'A média de {anos} ano(s) é de R$ {media}')
input()