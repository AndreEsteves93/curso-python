vel = int(input('Em qual velocidade estava o carro? '))
if vel > 80:
    print('Você foi multado em R${:.2f} por estar acima da velovidade permitida de 80km/h.'
          .format((vel - 80) * 7.00))
else:
    print('Tenha um bom dia!')
