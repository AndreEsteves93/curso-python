while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    for c in range(1, 11):
        r = c * n
        print(f'{n} x {c} = {r}')
print('Programa de tabuada encerrado.')
