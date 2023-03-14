temp = list()
princi = list()
menor = 0
maior = 0

while True:
    temp.append(str(input("nome: ")))
    temp.append(int(input("peso: ")))
    if len(princi) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior =  temp[1]
        if temp[1] < menor:
            menor = temp[1]        
    princi.append(temp[:])
    temp.clear()
    resposta = str(input("quer continuar?[s/n] "))
    if resposta in "nN":
        break
    
print(f"foram cadastradas {len(princi)} pessoas")

for p in princi:
    if p[1] == maior:
        print(f"o maior peso foi de {maior}kg {p[0]} ")
    if p[1] == menor:
        print(f"o menor peso foi de {menor}kg {p[0]} ")





