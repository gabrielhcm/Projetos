num2 = int(input("quantos numeros mostrar?"))
t1 = 0
t2 = 1
print(f"{t1} {t2}", end='')
contador = 3
while contador <= num2:

    t3 = t1 + t2
    print(f" {t3}",end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' fim')