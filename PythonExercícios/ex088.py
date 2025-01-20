from random import sample
from time import sleep
jogo = list()
jogos = list()
print('-' * 36)
print('{:^36}'.format('JOGA NA MEGA SENA'))
print('-' * 36)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 4,  f' SORTEANDO {q} JOGOS ', '=-' * 4)
for c in range(0, q):
    jogo = sample(range(1, 61), 6)
    jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
print('<' * 12, 'BOA SORTE!', '>' * 12)
print(jogos)
