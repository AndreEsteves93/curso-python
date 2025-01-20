largura = float(input('Qual a largura em metros da parede? '))
altura = float(input('Qual a altura em metros da parede? '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(tinta))
