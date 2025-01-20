def somar(a=0, b=0, c=0):
    """
    -> Faz e rotorna a soma de até 3 valores.
    Parâmetros opcionais. Caso a função não receba algum valor
    ele será considerado igual a zero.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: soma
    """
    s = a + b + c
    return s


# Programa principal
r1 = somar(2, 4, 6)
r2 = somar(b=3, c=20)
r3 = somar()
print(f'O resultado das somas foi {r1}, {r2} e {r3}.')