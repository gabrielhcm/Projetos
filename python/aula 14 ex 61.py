prim = int(input('digite o primeiro termo'))
razão = int(input('digite a razão'))
decimo = prim + (10-1) * razão

for c in range (prim,decimo+razão,razão):
  print('{} '.format(c))
print('acabou')  