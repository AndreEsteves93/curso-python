from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
if jogador > 3 or jogador < 0:
    print('Jogada inválida!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:
        if jogador == 0:
            print('Empate!')
        elif jogador == 1:
            print('Jogador venceu!')
        elif jogador == 2:
            print('Computador venceu!')
    elif computador == 1:
        if jogador == 0:
            print('Computador venceu!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('Jogador venceu!')
    elif computador == 2:
        if jogador == 0:
            print('Jogador venceu!')
        elif jogador == 1:
            print('Computador venceu!')
        elif jogador == 2:
            print('Empate!')
