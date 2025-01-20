alunos = list()
dado = list()
media = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    alunos.append(dado[:])
    dado.clear()
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
for c in range(0, len(alunos)):
    media.append((alunos[c][1] + alunos[c][2]) / 2)
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 22)
for a in range(0, len(alunos)):
    print(f'{a:<4}{alunos[a][0]:<10}{media[a]:>8}')
print('-' * 22)
while True:
    alu = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if alu == 999:
        break
    if alu <= len(alunos) - 1:
        print('-' * 30)
        print(f'Notas de {alunos[alu][0]} são {alunos[alu][1:]}')
        print('-' * 30)
    else:
        print('Número inválido!')
        print('-' * 30)
