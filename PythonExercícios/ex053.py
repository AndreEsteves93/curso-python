print('Detector de palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):  # ou inverso = junto [::-1]
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
