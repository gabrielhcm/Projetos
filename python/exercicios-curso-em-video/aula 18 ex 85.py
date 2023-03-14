
numeros = [[],[]]
pares = numeros[0]
impares = numeros[1]
contador = 1

for c in range(1,8):
    valor = int(input(f"digite o {contador} valor: "))
    contador+=1
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)    

print(pares)
print(impares)
