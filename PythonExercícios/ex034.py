sal = float(input('Qual seu salário? '))
if sal > 1250:
    print('Seu aumento será de R${:.2f}. \nSeu novo salário será R${:.2f}.'
          .format((sal * 1.1) - sal, (sal * 1.1)))
else:
    print('Seu aumento será de R${:.2f}. \nSeu novo salário será R${:.2f}.'
          .format((sal * 1.15) - sal, sal * 1.15))
