from datetime import date
atual = date.today().year

print('Confederação Nacional de Natação')
print('Categoria por idade')

ano = int(input('Qual seu ano de nascimento? '))
idade = atual - ano
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Você pertente a categoria MIRIM. Até 9 anos.')
elif idade <= 14:
    print('Você pertence a categoria INFANTIL. Até 14 anos.')
elif idade <= 19:
    print('VOcê pertence a categoria JUNIOR. Até 19 anos.')
elif idade <= 25:
    print('Você pertence a categoria SÊNIOR. Até 25 anos.')
else:
    print('Você pertence a categoria MASTER. Acima de 25 anos.')
