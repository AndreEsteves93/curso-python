n = int(input('Digite um número para \ncalcular seu fatorial: '))
r = n
f = 1
print('Calculando {}! = '.format(n), end='')
while r > 0:
    print('{}'.format(r), end='')
    print(' x ' if r > 1 else ' = ', end='')
    f *= r
    r -= 1
print('{}'.format(f))
