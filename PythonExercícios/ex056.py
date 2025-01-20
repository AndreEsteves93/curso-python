idatot = 0
FM = 0
velho = 0
nomevelho = ''
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    idatot += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'F' and idade < 20:
        FM += 1
    if p == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    else:
        if sexo == 'M' and idade > velho:
            velho = idade
            nomevelho = nome
print('A média de idade do grupo é de {:.2f} anos.'.format(idatot / 4))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(FM))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
