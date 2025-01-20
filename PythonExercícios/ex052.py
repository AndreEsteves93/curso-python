num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, cont))
if cont > 2:
    print('Portanto NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
