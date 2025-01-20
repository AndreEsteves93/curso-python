from random import randint
from time import sleep
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
num05 = randint(0, 10)
guess = int(input('Qual seu palpite? '))
print('Processando...')
sleep(2)
tent = 1
while guess != num05:
    if num05 > guess:
        print('Mais... Tente novamente.')
    else:
        print('Menos... Tente novamente.')
    guess = int(input('Qual seu palpite? '))
    tent += 1
    print('Processando...')
    sleep(1)
print('Parabéns! Você acertou com {} palpites!'.format(tent))

