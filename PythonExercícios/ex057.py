s = str(input('Informe seu sexo: [M/F] ')).upper()[0].strip()
while s not in 'MF':
    s = str(input('Sexo deve ser  "M" ou "F". Digite novamente: ')).upper()[0].strip()
print('Sexo {} registrado.'.format(s))
