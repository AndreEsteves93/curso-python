# o * é o desempacotamento. Transforma os valores passados numa tupla
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for v in num:
        print(f'{v} ', end='')
    print()

# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
