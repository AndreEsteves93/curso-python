def calcarea(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} é igual a {area}m²')


def titulo(txt):
    print('-' * 26)
    print(f'{txt:^26}')
    print('-' * 26)


# Programa Principal
titulo('Controle de Terrenos')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
calcarea(larg, comp)

