lista = list()
listap = list()
listaim = list()    

contador = 0
while True:
    numeros = int(input("digite um numero "))
    lista.append(numeros)
    escolha = str(input("quer continuar? [s/n] "))
    if escolha in "nN":
        break       
for c in lista:
    if c % 2 == 0:
        listap.append(c)
    elif c % 2 !=0:
        listaim.append(c)

print(f"a sua lista completa foi {lista}")
print(f"a lista com os numeros pares é {listap}")
print(f"a lista com os numeros impares é {listaim}")       