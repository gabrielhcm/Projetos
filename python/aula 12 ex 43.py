altura = float (input('digite a sua altura '))
peso = float (input('digite o seu peso '))

imc = peso/(altura* altura) # ou (altura** 2)

print('seu imc é {:.2f}'.format(imc))

if imc < 18.5:
    print('você esta abaixo do peso ideal')
elif imc > 18.5 and imc <= 25:
    print('Você esta no peso ideal')
elif imc > 25 and imc <= 30:
  print('sobrepeso')
elif imc > 30 and imc <= 40:
    print('obesidade')    
else:
 print('obesidade morbida')       
  

