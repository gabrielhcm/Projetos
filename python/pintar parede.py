altura = float (input('qual a altura da parede em metros? '))
largura = float (input('qual a largura da parede? em metros? '))

area = altura * largura

tinta = area/2

print(' a area total  da parede é {}, será preciso gastar {} de tinta para poder pintar a parede'.format(area, tinta ))