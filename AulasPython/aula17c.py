a = [2, 3, 4, 7]
# Essa forma cria uma ligação entre as listas > b = a
# Na forma abaixo cria-se uma cópia
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')