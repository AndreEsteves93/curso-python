dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
price = (60 * dias) + (km * 0.15)
print('O preço a pagar por {} dias tendo rodado {}Km é R${:.2f}'.format(dias, km, price))
