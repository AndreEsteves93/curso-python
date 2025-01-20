def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


# Programa Principal
print(voto(int(input('Em que ano a pessoa nasceu? '))))

