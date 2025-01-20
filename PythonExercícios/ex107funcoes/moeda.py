def metade(preco):
    res = preco / 2
    return res


def dobro(preco):
    res = preco * 2
    return res


def aumentar(preco, taxa):
    res = preco + (preco / 100 * taxa)
    return res


def diminuir(preco, taxa):
    res = preco - (preco / 100 * taxa)
    return res
