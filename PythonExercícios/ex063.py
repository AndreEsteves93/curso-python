c = int(input('Quantos termos você quer mostrar? '))
x = 0
y = 1
r = 1
print('{} -> {} -> '.format(x, y), end='')
while c >= 3:
    r = x + y
    x = y
    y = r
    c -= 1
    print('{} -> '.format(r), end='')
print('FIM')
