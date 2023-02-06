num1 = float(input('digite o primeiro numero '))
num2 = float(input('digite o segundo numero '))
num3 = float(input('digite o terceiro numero' ))

nummenor = 0
nummaior = 0

if num1 > num2 and num3:
  nummaior = num1
elif num2 >num1 and num3:
  nummaior = num2
elif num3 > num2 and num1:
  nummaior = num3
else:
  ('erro')

if num1 < num2 and num1<num3:
  nummenor = num1
elif num2 < num3 and num3<num1:
  nummenor = num2
elif num3 < num1 and num3<num2:
  nummenor = num3  
else:
 ('erro') 

print(' o maior numero é {} e o menor numero é {}'.format(nummaior, nummenor))        