cidaden = str(input('Digite o nome da cidade ')).strip()

cidaden = cidaden.find('Santo')
#cidaden.upper()

if cidaden == -1:
 print('não começa')
elif cidaden == 0:
 print('começa')  
else:  
 print('não começa')

 # forma preguiçosa de se usar .find