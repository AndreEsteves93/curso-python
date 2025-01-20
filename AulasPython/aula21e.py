def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa Principal
num = int(input('Digite um número para descobrir se é par ou ímpar: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
