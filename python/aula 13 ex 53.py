frase = str(input('digite uma frase ')).strip().upper()

palavras = frase.split() #separou em um vetor

junto = ''.join(palavras) #juntou tudo pra tirar os espaços entre os vetores
inverso = '' 

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('é um palindromo')        
else:
    print('não é um palindromo')    