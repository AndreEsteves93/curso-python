maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Quanto pesa a {}ª pessoa? Kg'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('''O maior peso lido foi de {}Kg.
O menor peso lido foi de {}Kg'''.format(maior, menor))
