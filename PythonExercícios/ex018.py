from math import sin, cos, tan, radians
a = float(input('Digite o valor do angulo: '))
r = radians(a)
print('Seno = {:.2f}. \nCosseno = {:.2f}. \nTangente = {:.2f}.'.format(sin(r), cos(r), tan(r)))
