valorcasa = float (input('qual o valor da casa?'))
salario = float (input('qual o seu salario?'))
anos = float(input('vai pagar em quantos anos?'))

anosmes = anos * 12 

prestam = valorcasa / anosmes

min = salario * 30 / 100

if prestam > salario:
 print('Emprestimo negado!')
else:
 print('o valor da prestação será: R${:.2f} Reais'.format(prestam)) 