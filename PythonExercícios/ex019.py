'''import random
sort = random.choice(['Andre', 'Débora', 'Bianca', 'Vinicius'])
print('{} vai apagar o quadro.'.format(sort))'''
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('{} vai apagar o quadro.'.format(escolhido))
