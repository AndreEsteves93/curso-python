aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 20)
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO!'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO!'
else:
    aluno['situação'] = 'REPROVADO!'
for k, v in aluno.items():
    print(f'{"- ":>4}{k} é igual a {v}')
