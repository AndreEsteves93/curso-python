#\033[estilo; texto; backm
#\033[0;33;44m
# estilo -> 0 none, 1 bold, 4 underline, 7 negative
# texto -> 30 a 37
# back -> 40 a 47
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7mOlá, Mundo!\033[m')
print('\033[7;33mOlá, Mundo!\033[m')
print('\033[1;32;41mOlá, Mundo!\033[m')
nome = 'Andre'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'
      .format(cores['amarelo'], nome, cores['limpa']))
