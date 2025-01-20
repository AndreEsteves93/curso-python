from random import randint
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadas.items():
    print(f'   O {k} tirou {v} no dado.')
ranking = sorted(jogadas.items(), key=itemgetter(1),  reverse=True)
print('Ranking dos jogadores:')
for c, v in enumerate(ranking):
    print(f'   {c+1}º lugar: {v[0]} com {v[1]}')
