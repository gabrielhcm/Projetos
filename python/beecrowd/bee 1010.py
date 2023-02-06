num = str(input())
num2 = str(input())

numb = num.split(" ")
numc = num2.split(" ")

val1 =  float (numb[1])
val2 =  float (numb[2])
val3 =  float (numc[1])
val4 =  float (numc[2])

preçof =  (val1 * val2) + (val3* val4)

print('VALOR A PAGAR: R$ {:.2f}'.format(preçof))
