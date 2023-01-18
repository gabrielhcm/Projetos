cidaden = str(input('Digite o nome da cidade '))

cidaden = cidaden.find('Santo')

if cidaden == -1:
 print('não começa')
elif cidaden == 0:
 print('começa')  
else:  
 print('não começa')

 # forma preguiçosa de se usar .find