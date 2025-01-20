def leiaint(txt):
    ok = False
    valor = 0
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
