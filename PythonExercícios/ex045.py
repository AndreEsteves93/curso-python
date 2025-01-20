from random import randint
print('JOKENPÔ')
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
hum = int(input('Qual você escolhe? '))
cpu = randint(1, 3)
if hum == 1 and cpu == 2:
    print('Você escolheu PEDRA e o computador PAPEL. \nVocê PERDEU!')
elif hum == 1 and cpu == 3:
    print('Você escolheu PEDRA e o computador TESOURA. \nVocê GANHOU!')
elif hum == 2 and cpu == 1:
    print('Você escolheu PAPEL a o computador PEDRA. \nVocê GANHOU!')
elif hum == 2 and cpu == 3:
    print('Você escolheu PAPEL e o computador TESOURA. \nVocê PERDEU!')
elif hum == 3 and cpu == 1:
    print('Você escolheu TESOURA e o computador PEDRA. \nVocê PERDEU!')
elif hum == 3 and cpu == 2:
    print('Você escolheu TESOURA e o computador PAPEL. \nVocê GANHOU!')
elif hum == cpu:
    print('Ambos escolheram o mesmo. EMPATE!')
else:
    print('Por favor, escolha um valor válido de 1 a 3 para jogar.')
