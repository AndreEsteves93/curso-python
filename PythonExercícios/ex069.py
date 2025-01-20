maior = homem = menina = 0
while True:
    print('-' * 21)
    print(' CADASTRE UMA PESSOA')
    print('-' * 21)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menina += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {homem} homens cadastrados
E temos {menina} mulheres com menos de 20 anos.''')
