from time import sleep


def maior(* valores):
    mai = 0
    print('Analisando os valores passados...')
    for n in valores:
        print(f'{n}', end=' ')
        sleep(0.5)
        if n > mai:
            mai = n
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')
    print('-=' * 30)


# Programa principal
print('-=' * 30)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
