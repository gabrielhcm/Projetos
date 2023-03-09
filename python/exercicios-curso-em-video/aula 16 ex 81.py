lista = list()
while True:
    numeros = int(input("digite um numero"))
    lista.append(numeros)
    escolha = str(input("quer continuar? [s/n]"))
    if escolha in "nN":
        break    
    
print(f"foram digitados {len(lista)} numeros")
lista.sort(reverse=True)
print(f" a lista de forma decrescente é {lista}")    
    
if lista.count(5):
    print("o valor 5 foi digitado e está na lista")
else:
    print("o valor 5 não está na lista")

