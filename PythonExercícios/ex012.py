price = float(input('QUal é o preço do produto? R$'))
desc = price * 0.95 #ou então desc = price - (price * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'
      .format(price, desc))
