lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        lista.sort(reverse=True)
        break
print('-' * 35)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('Não tem o valor 5 na lista!')
