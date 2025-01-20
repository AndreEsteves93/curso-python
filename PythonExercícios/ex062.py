pri = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
c = 10
termos = 0
while c != 0:
    while c > 0:
        print('{} -> '.format(pri), end='')
        pri += razao
        c -= 1
        termos += 1
    print('PAUSA')
    c = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(termos))
