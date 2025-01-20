precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
          'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 36)
print('{:^36}'.format('LISTAGEM DE PREÇOS'))
print('-' * 36)
for p in precos:
    if precos.index(p) % 2 == 0:
        print(f'{p}', end='')
        print('.' * (26 - len(p)), end='')
    else:
        print('R$', end='')
       # print(' ' * 1, end='')
       # print(f'{p}')
        print('{:>7}'.format(f'{p:.2f}'))
print('-' * 36)
