s = d = str(input("""Qual é o seu sexo
  [M] -> Masculino
  [F] -> Feminino
  """))
while s not in 'MmFf':
    s = d = str(input("""Qual é o seu sexo
    [M] -> Masculino
    [F] -> Feminino
    """))
print('FIM')