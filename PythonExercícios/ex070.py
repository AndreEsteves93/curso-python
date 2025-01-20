print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)
total = caro = quant = barato = 0
prodbarato = ''
while True:
    prod = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço: R$'))
    total += preco
    quant += 1
    if preco > 1000:
        caro += 1
    if quant == 1 or preco < barato:
        prodbarato = prod
        barato = preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {caro} custando mais de R$1000.00')
print(f'O produto mais barato foi {prodbarato} que custa R${barato:.2f}')
