tot = vezes = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    tot += n
    vezes += 1
print(f'Você digitou {vezes} números e a soma entre eles é {tot}.')
