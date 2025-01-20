from time import sleep

from PythonExercícios.ex115b.lib.arquivo import *
from PythonExercícios.ex115b.lib.interface import *

arq = 'cursoemvideo.txt'

if not arq(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo.
        lerArquivo(arq)
    if resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        if resposta <= 0 or resposta >= 4:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
