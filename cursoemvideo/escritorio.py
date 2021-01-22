da = str(input('Digite Bom dia/ Boa Tarde / Boa Noite: '))
n = int(input('digite o numero do apartamento: '))
b = str(input('Qual é o bloco A ou B: '))
ven = str(input('Quais são as cotas: '))
d = float(input('Qual é o valor do débito? R$'))
p = float(input('Quanto de honorários? '))
boleto = str(input('Vencimento do boleto: '))
h = d * (p / 100)
v = d + h
print(""" {} Ellen!

Condomínio Vila Nova Ipiranga
Referente: Apartamento {}, bloco {}

Peço a emissão de boletos conforme segue:

Cotas condominiais vencidas em {}

Valor do débito atualizado R$ {:.2f}
Honorários R$ {:.2f}
-----------------------------------------
Total R$ {:.2f} com vencimento para {}

Por fim, peço a gentileza de enviar este boleto no meu e-mail.

Obrigado!

Ronaldo Moraes Petruitis
Advogado""".format(da, n, b, ven, d, h, v, boleto))

input()