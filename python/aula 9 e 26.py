frase = str(input(' digite uma frase ')).strip().upper()

numn = frase.count('A')

numcome = frase.find('A')+1

numfinal = frase.rfind('A')

print(numn)
print(numcome)
print(numfinal)