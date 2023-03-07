numeros=(
'zero',
 'um',
'dois',
 'três',
 'quatro',
 'cinco',
 'seis',
 'sete',
 'oito',
 'nove',
 'dez',
 'onze',
 'doze',
 'treze',
 'quatorze',
 'quinze',
 'dezesseis',
 'dezessete',
 'dezoito',
 'dezenove',
 'vinte',
)

conti = ""
while True:
    digitado = int(input("digite um numero entre 0 e 20 "))
    if digitado < 0 or digitado > 20:
        print("digite um numero entre 0 e 20 ")
    else:     
        print(numeros[digitado])
        conti = str(input('quer continuar?[s/n]').upper())
        if conti != "N" or "S":
            print("não entendi, quer continuar?")
    if conti == "N":
        print("programa finalizado")
        break
       