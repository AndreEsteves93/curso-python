import aula22uteis
from uteis import numeros

num = int(input('Digite um valor: '))
fat = aula22uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {aula22uteis.dobro(num)}.')
print(f'O número {num} é {numeros.ispar(num)}')
