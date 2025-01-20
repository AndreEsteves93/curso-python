def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um número inteiro válido')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return num


def leiastr(txt):
    while True:
        try:
            nome = str(input(txt))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um nome válido')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o nome')
            return 'desconhecido'
        else:
            return nome

def escolha(txt):
    mostrarmenu()
    pessoa = dict()
    lista = list()
    while True:
        opcao = leiaint(txt)
        if opcao == 1:
            if len(pessoa) == 0:
                print('Ainda não temos nenhuma pessoa cadastrada')
            else:
                mostrartabela(pessoa, lista)
        if opcao == 2:
            cadastra(pessoa, lista)
        if opcao == 3:
            print('-' * 40)
            print(f'{"FINALIZANDO O PROGRAMA...":^40}')
            print(f'{"ATÉ A PRÓXIMA":^40}')
            print('-' * 40)
            break
        else:
            mostrarmenu()


def cadastra(pessoa, lista):
    print('-' * 40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' * 40)
    nome = leiastr('Nome: ')
    idade = leiaint('Idade: ')
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    lista.append(pessoa.copy())
    print(f'Novo registro de {nome} adicionado')


def mostrartabela(pessoa, lista):
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    for c, p in enumerate(lista):
        for v in p.values():
            print(f'{str(v):>10}', end=' ')
        print('anos')
    print('-' * 40)


def mostrarmenu():
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 40)
