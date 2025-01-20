from random import randint
from time import sleep
v = 0
while True:
    n = int(input('Diga um valor de 0 a 5: '))
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    comp = randint(0, 5)
    soma = comp + n
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {comp}. Total de {soma} deu PAR.')
        resultado = 'P'
    else:
        print(f'Você jogou {n} e o computador {comp}. Total de {soma} deu ÍMPAR.')
        resultado = 'I'
    if resultado == opcao:
        v += 1
        print('Você VENCEU!\nVamos jogar novamente...')
        sleep(2)
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {v} vezes')
