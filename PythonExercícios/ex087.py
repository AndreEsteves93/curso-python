matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somapar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
print('-' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
print('-' * 40)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
#qualquer coisa dar uma olhada na resolução diferente do guanaba