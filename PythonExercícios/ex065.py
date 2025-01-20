vezes = soma = med = maior = menor = 0
c = 's'
while c in 'Ss':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).strip()[0]
    soma += n
    vezes += 1
    med = soma / vezes
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
print('Você digitou {} números e a média foi {:.2f}.'.format(vezes, med))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
