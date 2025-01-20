print('Analisador de triângulos V2.0')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem fomar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Não formam um triângulo.')
