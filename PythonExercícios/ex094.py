pessoa = dict()
lista = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    cont = ' '
    while cont not in 'SsNn':
        cont = (str(input('Deseja continuar? [S/N] '))).strip().upper()[0]
    if cont in 'Nn':
        break
print('-=' * 30)
print(f' - O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f' - A média de idade é de {media:5.2f} anos.')
print(' - As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(' - Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


