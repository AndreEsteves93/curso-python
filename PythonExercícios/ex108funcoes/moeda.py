def metade(preco=0):
    res = preco / 2
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def aumentar(preco=0, taxa=0):
    res = preco + (preco / 100 * taxa)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco / 100 * taxa)
    return res


def moeda(preco=0, moeda='R$'):
    formatado = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatado
