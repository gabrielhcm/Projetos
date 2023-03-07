valores= (int(input("digite quatro valores")),
            int(input("digite quatro valores")),
            int(input("digite quatro valores")),
            int(input("digite quatro valores")))




print(f"o numero 9 foi digitado {valores.count(9)} vezes")
print(f"o numero 3 foi digitado na posição {valores.index(3)}")
print("os numeros pares foram")
for n in valores:
    if n% 2 == 0:
        print(n)
