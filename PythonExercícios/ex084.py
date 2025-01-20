pessoas = list()
dado = list()
leve = list()
pesado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
for c, p in enumerate(pessoas):
    if c == 0 or p[1] < menor:
        menor = p[1]
    elif p[1] > maior:
        maior = p[1]
for p in pessoas:
    if p[1] == menor:
        leve.append(p[0])
    elif p[1] == maior:
        pesado.append(p[0])
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {pesado}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {leve}')
