def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


# Programa Principal
print(fatorial(5, show=True))
