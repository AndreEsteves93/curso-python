def fatorial(num=1):
    """
    Calcula o fatorial de um número.
    :param num: número inteiro
    :return: fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# Programa Principal
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(0)
print(f'Os resultados são {f1}, {f2} e {f3}.')
