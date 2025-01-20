jogador = {}
gols = []
lista = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    qnt = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, qnt):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    # também poderia ser sum(gols) para ter o total de gols
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    cont = ' '
    while cont not in 'SsNn':
        cont = (str(input('Deseja continuar? [S/N] '))).strip().upper()[0]
    if cont in 'Nn':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<12}', end='')
print()
print('-' * 40)
for c, j in enumerate(lista):
    print(f'{c:>2}', end='  ')
    for v in j.values():
        print(f'{str(v):<12}', end='')
    print()
print('-' * 40)
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jog in range(0, len(lista)):
        print(f'O jogador {lista[jog]["nome"]} jogou {len(lista[jog]["gols"])} partidas')
        for i, v in enumerate(lista[jog]['gols']):
            print(f'   => Na partida {i + 1}, fez {v} gols.')
        print(f'Foi um total de {lista[jog]["total"]} gols.')
    elif jog == 999:
        print('Programa finalizado')
        break
    else:
        print(f'Erro! Não existe jogador com o código {jog}')
