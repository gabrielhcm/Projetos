lista = list()

for  v in range(0,5):
    num = int(input("digite um numero "))

if v == 0 :
    lista.append(num)
    numero = num
    print("adicionado no final da lista")
elif num > lista[-1]:
    lista.append(num)
