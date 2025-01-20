from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(maiores, menores))
