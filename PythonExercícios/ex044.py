price = float(input('Qual o preço do produto? R$'))
print('Formas de pagamento: \n[ 1 ] À vista no dinheiro ou cheque. '
      '\n[ 2 ] À vista no cartão. \n[ 3 ] Em até 2x no cartão. \n[ 4 ] 3x ou mais no cartão.')
metodo = int(input('Qual será a forma de pagamento? '))
if metodo == 1:
    pag = price * 0.90
    print('Seu produto de R${:.2f} saíra por R${:.2f}'.format(price, pag))
elif metodo == 2:
    pag = price * 0.95
    print('Seu produto de R${:.2f} saíra por R${:.2f}'.format(price, pag))
elif metodo == 3:
    pag = price / 2
    print('Seu produto de R${:.2f} saíra por duas vezes de R${:.2f}'.format(price, pag))
elif metodo == 4:
    parcela = int(input('Em quantas parcelas? '))
    pag = price * 1.20 / parcela
    print('Seu produto de R${:.2f} saíra por {} parcelas de R${:.2f}'.format(price, parcela, pag))
else:
    print('Metodo de pagamento inválido')
