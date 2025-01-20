num = []
par = []
impar = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}o. valor: '))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()
num.append(par[:])
num.append(impar[:])
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
