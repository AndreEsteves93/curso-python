def leiaint(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            return num
        else:
            print('ERRO! Digite um número inteiro válido.')


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
