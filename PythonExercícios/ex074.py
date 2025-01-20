from random import randint
maior = menor = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
for c in n:
    if c > maior:
        maior = c
    if c < menor or menor == 0:
        menor = c
print(f'Os valores sorteados foram {n}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
