import math

cop = float(input(' digite o comprimento do cateto oposto de um triangulo retangulo'))
cad = float(input('digite o comprimento do cateto adjacente de um triangulo retangulo'))

hi = math.hypot(cop, cad)

print('a hipotenusa vai medir {:.2f}'.format(hi))