valores = [
        int(input("digite um numero ")),
        int(input("digite um numero ")),
        int(input("digite um numero ")),
        int(input("digite um numero ")),
        int(input("digite um numero ")),
        ]

maior = 0
menor = valores[0]
pos1 = 0
pos2 = 0

for v in valores:

    if v > maior:
        maior = v
    if v <= menor:
        menor = v

for n in valores:
    if n ==maior:
        pos1 = n
    if n == menor:
     pos2 = n    


print(f"o maior valor digitado foi {maior} que está na posição {pos1} e o menor valor digitado foi {menor} que está na posição {pos2}")