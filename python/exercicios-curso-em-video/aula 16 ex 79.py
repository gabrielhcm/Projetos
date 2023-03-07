valores = list()

while True:
    test = int(input("digite um numero "))
    if test not in valores:
        valores.append(test)
        print("valor adicionado")
    else:
        print('valor ja foi inserido')
    perg = str(input("quer continuar? [s/n]")).upper()
    if perg in "Nn":
        break
valores.sort()    
print(valores)    