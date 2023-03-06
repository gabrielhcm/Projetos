soma = 0
maior = 0
menor = 0
total = 0
contador = 0
media = 0
resposta = "S"
while resposta == "S":
    num = int(input("digite um numero! "))
    resposta = str(input("quer continuar? s/n " )).upper().strip()[0]
    total = total + num
    contador += 1
    if contador == 1:
        menor = num 
        maior = num
    else:    
        if num > maior:
            maior = num 
        if num < menor:
            menor = num 

    media = total / contador

print(f"o maior numero digitado foi {maior} e o menor numero digitado foi {menor} você digitou {contador} numeros e a media dos numeros digitados foi {media:.1f}")