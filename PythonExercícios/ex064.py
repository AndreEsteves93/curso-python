tot = vezes = n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        tot += n
        vezes += 1
print('Você digitou {} números e a soma entre eles é {}.'.format(vezes, tot))
