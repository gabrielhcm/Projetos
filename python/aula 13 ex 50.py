soma = 0
count = 0


for c in range (1,7):
  num = int(input('Digite o {} '.format(c)))
  if num % 2==0:  
   soma = soma + num
   count = count + 1
print('você informou {} e a soma foi {}'.format(count, soma))  