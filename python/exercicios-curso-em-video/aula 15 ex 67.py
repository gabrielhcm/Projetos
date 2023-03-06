while True:
    contador = 0
    mult = 0
    num = int(input("digite um numero para ver a tabuada "))
    if num < 0:
        print('você encerrou o programa!')
        break
        
    while contador < 10:
        contador += 1
        mult = num * contador
        print(f"{num} x {contador} = {mult} ")
        