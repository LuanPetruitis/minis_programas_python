preco = float(input('Qual é o valor da casa:  R$ '))
salario = float(input('Qual é o seu salário:  R$'))
tempo = float(input('Quantos anos você quer pagar:  '))
entrada = float(input('Qual é o valor que você pode dar de entrada'))
p = preco / (tempo*12)
if p <= (salario - entrada) * (30/100):
    print('O empréstimo será consedido, você deve pagar R${}'. format(p))
else:
    print('O emprestimo não será concedido')