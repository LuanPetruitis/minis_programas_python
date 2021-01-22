def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, você pode escolher se quer votar ou não'
    else:
        return f'Com {idade} anos, você deve votar'

# Progrma Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))