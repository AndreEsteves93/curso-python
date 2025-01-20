from datetime import date
atual = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade < 18:
    print('Você deverá se alistar daqui a {} anos. \nSeu alistamento será em {}.'
          .format(18 - idade, nascimento + 18))
elif idade == 18:
    print('Você deve se alistar esse ano.')
else:
    print('Você está {} anos atrasado para seu alistamento! \nSeu alistamento foi em {}.'
          .format(idade - 18, nascimento + 18))
