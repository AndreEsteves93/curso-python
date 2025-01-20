from datetime import date
ano = date.today().year
trabalhador = {'nome': str(input('Nome: ')),
               'idade': ano - int(input('Ano de nascimento: ')),
               'ctps': int(input('Carteira de trabalho (0 não tem): '))}
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (35 - (ano - trabalhador['contratação']))
print('-=' * 20)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')


