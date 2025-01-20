pri = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
for c in range(pri, pri + razao * 10, razao):
    print(c, end=' -> ')
print('ACABOU')
