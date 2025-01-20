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
