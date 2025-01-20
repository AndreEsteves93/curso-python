expressão = str(input('Digite uma expressão: '))
if expressão.count('(') == expressão.count(')'):
    print('Sua expressão é válida')
else:
    print('Sua expressão está errada!')
print(expressão)

