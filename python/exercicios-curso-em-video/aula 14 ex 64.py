num = 0
contador = 0
soma = 0

while num != 999:
    
    num = int(input("digite um numero ou 999 para parar! "))
    soma = soma + num
    
    contador += 1

print(f"foram digitados {contador-1} numeros e a soma dos numeros digitados foi: {soma-999}")    