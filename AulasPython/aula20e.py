def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é igual a {s}')


# Programa Principal
soma(3, 7)
soma(5, 6, 3, 4, 7)
soma(5, 5)
