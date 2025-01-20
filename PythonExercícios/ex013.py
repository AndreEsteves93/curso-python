sal = float(input('Qual é o salário do funcionário? R$'))
aum = sal + (sal * 15 / 100)
print('Um funcionário que recebia R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, aum))
