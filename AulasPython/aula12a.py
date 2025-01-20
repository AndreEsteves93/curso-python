nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Tu não é aquele professor?')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Débora Jéssica Bianca':
    print('Belo nome feminino')
else:
    print('bom nome!')
print('Tenha um bom dia, {}!'.format(nome))
