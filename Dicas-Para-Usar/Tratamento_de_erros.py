# Pode ter mais que um except

try:
    a = int(input('Digite:'))    
    b = int(input('Digite:'))
    r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um problema , foi {erro.__class__}')
else:
    print(r)    
finally:
    print('Volte sempre! Muito obrigado')