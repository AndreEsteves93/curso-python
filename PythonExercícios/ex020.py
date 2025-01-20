'''import random
alunos = 'Andre, Débora, Bianca, Vinicius' .split()
random.shuffle(alunos)
print(alunos)'''
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
