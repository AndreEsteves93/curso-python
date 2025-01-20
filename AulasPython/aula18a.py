teste = list()
teste.append('Andre')
teste.append(31)
galera = list()
galera.append(teste[:])
teste[0] = 'Débora'
teste[1] = 30
galera.append(teste[:])
print(galera)
