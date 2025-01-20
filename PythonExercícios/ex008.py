n = float(input('Quantos metros você deseja converter? '))
#c = n * 100
#m = n * 1000
#print('Esse valor correnponde a {} centimetros ou {} milimetros'.format(c, m))
print('{} metros corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'
      .format(n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
