print('\033[1;34m**' * 11)
print('Calculadora de média')
print('**' * 11)

n1 = float(input('\033[mNota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
med = (n1 + n2) / 2
print('Sua média foi de {:.1f}.'.format(med))
if med < 5.0:
    print('Você está \033[1;31mREPROVADO\033[m!')
elif med < 7.0:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m!')
else:
    print('Parabéns! Você está \033[1;32mAPROVADO\033[m!')
