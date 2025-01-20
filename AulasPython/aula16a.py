lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
# desconsidera o último
print(lanche[2:])
print(lanche[:2])
# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refrigerante' vai dar erro

# for in
for comida in lanche:
    print(f'Eu vou comer {comida}')

# for trabalhando com range len
for cont in range(0, len(lanche)):
    print(lanche[cont])

# para pegar a posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba')
