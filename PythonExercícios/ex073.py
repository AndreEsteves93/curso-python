times_brasileirao = ('Palmeiras', 'Botafogo', 'Internacional', 'Fortaleza', 'Flamengo', 'São Paulo',
                     'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG', 'Vasco', 'Vitória', 'Athletico-PR',
                     'Grêmio', 'Fluminense', 'Juventude', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times_brasileirao}')
print('-=' * 15)
print(f'Os 5 primeiros são {times_brasileirao[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times_brasileirao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print('-=' * 15)
print(f'O Fluminense está na {times_brasileirao.index("Fluminense")+1}ª posição')
