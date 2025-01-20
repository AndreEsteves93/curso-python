def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um número inteiro válido')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return num


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um número real válido')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return num


# Programa Principal
numfloat = leiafloat('Digite um número real: ')
numint = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número inteiro {numint} e o número real {numfloat}.')
