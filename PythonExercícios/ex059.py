from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
Escolha uma opção:  '''))
    if menu == 1:
        r = n1 + n2
        print('A soma é {}.'.format(r))
    elif menu == 2:
        r = n1 * n2
        print('A multiplicação é {}'.format(r))
    elif menu == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print('O maior valor é {}'.format(r))
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Programa finalizado.')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
