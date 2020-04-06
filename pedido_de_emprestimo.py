preco = float(input('qual é o valor da casa:  R$ '))
salario = float(input('qual é o seu salário:  R$'))
tempo = float(input('quantos anos você vai pagar:  '))
entrada = float(input('qual é o valor que você pode dar de entrada'))
p = preco / (tempo*12)
if p <= (salario - entrada) * (30/100):
    print('O empréstimo será consedido, você deve pagar R${}'. format(p))
else:
    print('O emprestimo não será concedido')