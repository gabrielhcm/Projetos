num = 0
contador = 0
soma = 0

while True:
    
    num = int(input("digite um numero ou 999 para parar! "))
    if num == 999:
        break
    soma = soma + num
    
    contador += 1

print(f"foram digitados {contador} numeros e a soma dos numeros digitados foi: {soma}")    