distancia = float(input('Digite a distancia da viagem em Km '))

if distancia <= 200:
 distancia = distancia * 0.50
else:
  distancia * 0.45
  distancia = distancia * 0.45
  
print( 'O custo da viagem foi R${:.2f} Reais'.format(distancia))   

