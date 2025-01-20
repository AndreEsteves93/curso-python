pri = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
c = 10
while c > 0:
    print('{} -> '.format(pri), end='')
    pri += razao
    c -= 1
print('ACABOU')
