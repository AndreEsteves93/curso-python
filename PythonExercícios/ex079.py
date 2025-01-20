lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        lista.sort()
        break
print('-' * 35)
print(f'Você digitou os valores {lista}')
