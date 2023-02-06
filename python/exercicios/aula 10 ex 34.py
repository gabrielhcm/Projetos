salario = float(input('digite o seu salario '))

if salario > 1.250:
  salario = salario + (salario * 0.10)

else:
  salario = salario + (salario * 0.15)

print('o seu salario com o devido aumento é {:.2f}'.format(salario))  
