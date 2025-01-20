def metade(preco=0, formata=False):
    res = preco / 2
    return res if formata is False else moeda(res)


def dobro(preco=0, formata=False):
    res = preco * 2
    if formata:
        res = moeda(res)
    return res


def aumentar(preco=0, taxa=0, formata=False):
    res = preco + (preco / 100 * taxa)
    return res if not formata else moeda(res)


def diminuir(preco=0, taxa=0, formata=False):
    res = preco - (preco / 100 * taxa)
    if formata:
        res = moeda(res)
    return res


def moeda(preco=0, moeda='R$'):
    formatado = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatado


def resumo(preco=0, taum=0, tred=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taum}% de aumento: \t{aumentar(preco, taum, True)}')
    print(f'{tred}% de redução: \t{diminuir(preco, tred, True)}')
    print('-' * 30)
