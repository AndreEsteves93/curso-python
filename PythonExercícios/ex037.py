print('\033[36m=\033[m' * 27)
print('\033[36mConversor de base númerica\033[m')
print('\033[36m=\033[m' * 27)

num = int(input('Digite o número inteiro que deseja converter: '))
qualb = int(input('Digite [ 1 ] para binário \nDigite [ 2 ] para octal \nDigite [ 3 ] para hexadecimal '
                  '\nPara qual deseja converter? '))
if qualb == 1:
    print('{} convertido para BINÁRIO é a igual a {}'.format(num, bin(num)[2:]))
elif qualb == 2:
    print('{} convertido para OCTAL é a igual a {}'.format(num, oct(num)[2:]))
elif qualb == 3:
    print('{} conventido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Você digitou uma opção inválida!')
