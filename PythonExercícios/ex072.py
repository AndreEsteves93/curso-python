numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
                       'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
                       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros_por_extenso[n]}')
        cont = ' '
        while cont not in 'SN':
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont == 'N':
            break
    if n > 20 or n < 0:
        print('Tente novamente. ', end='')
