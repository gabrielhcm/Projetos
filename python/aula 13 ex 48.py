soma = 0
contador = 0
print('os numeros impares são')  
for c in range(1, 501, 2):
    if(c%3) ==0:
     soma = soma + c
     contador = contador + 1
print('a soma de {} valores é {}'.format(contador,soma))

