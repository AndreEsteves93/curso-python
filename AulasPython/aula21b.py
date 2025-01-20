def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de até 3 valores e mostra o resultado na tela.
    Parâmetros opcionais. Caso a função não receba algum valor
    ele será considerado igual a zero.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}.')


# Programa Principal
somar(2, 4)
somar(c=3, b=5)
