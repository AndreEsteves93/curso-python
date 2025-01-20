from random import randint
from time import sleep
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
num05 = randint(0, 5)
guess = int(input('Qual seu palpite? '))
print('Processando...')
sleep(2)
if guess == num05:
    print('Parabéns! Você acertou!')
else:
    print('Errou! eu pensei no {}. Tente novamente.'.format(num05))
