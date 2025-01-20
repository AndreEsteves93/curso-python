print('-' * 30)
print('{:^30}'.format('BANCO ESTEVES'))
print('-' * 30)
c50 = c20 = c10 = c01 = 0
n = int(input('Qual valor deseja sacar? R$'))
while n >= 50:
    n -= 50
    c50 += 1
while n >= 20:
    n -= 20
    c20 += 1
while n >= 10:
    n -= 10
    c10 += 1
while n >= 1:
    n -= 1
    c01 += 1
if c50 > 0:
    print(f'Total de {c50} cédulas de R$50')
if c20 > 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10')
if c01 > 0:
    print(f'Total de {c01} cédulas de R$1')
print('-' * 30)
print('Volte sempre ao BANCO ESTEVES! Tenha um bom dia!')
