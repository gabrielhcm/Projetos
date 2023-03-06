from random import randint
poui = ""
contador = 0
while True:
    pcescolha = randint(1,1000)
    val = int(input("digite um valor:"))
    escolha = str(input("par ou impar?[P/I] ")).upper().strip()[0]
    impapar = ""
    total = pcescolha + val
    resultado = total % 2
    if resultado != 0:
        impapar ="I"
        poui = "Impar"
    else:
        impapar = "P" 
        poui = "Par"
    print(f"você jogou {val} e o computador {pcescolha} o total foi {total} deu {poui}.")         
    if escolha != impapar:
        print("você perdeu!")
        break
    else:
        print("voce ganhou!")
        print("vamos jogar de novo...")
        contador+=1
      
print(f"game over! Você venceu {contador} vezes!")