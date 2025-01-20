lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

