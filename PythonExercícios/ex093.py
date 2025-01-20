jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
qnt = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, qnt):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += gols[c]
jogador['gols'] = gols[:]
# também poderia ser sum(gols) para ter o total de gols
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
