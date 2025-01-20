d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print('Sua viagem custará R${:.2f}.'.format(d * 0.50))
else:
    print('Sua viagem custará R${:.2f}.'.format(d * 0.45))
