valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')

print('\n')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

