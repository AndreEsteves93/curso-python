n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    mult = c * n
    print('{} x {} = {}'.format(n, c, mult))
