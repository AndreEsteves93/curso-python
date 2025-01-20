def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações dos alunos
    :param valores: Uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre as notas do aluno
    """
    cont = maior = menor = soma = 0
    aluno = dict()
    tot = len(valores)
    aluno['total'] = tot
    for n in valores:
        soma += n
        if cont == 0 or n < menor:
            menor = n
        if n > maior:
            maior = n
        cont += 1
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['média'] = soma / len(valores)
    if sit:
        if aluno['média'] >= 8:
            aluno['situação'] = 'Boa'
        elif aluno['média'] >= 6:
            aluno['situação'] = 'Razoável'
        else:
            aluno['situação'] = 'Ruim'
    return aluno


resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
help(notas)
