nome = str(input('Qual seu nome completo? ')).strip()
div = nome.split()
print('Primeiro nome: {} \nÚltimo nome: {}'.format(div[0], div[-1]))
