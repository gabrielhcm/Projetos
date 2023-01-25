from datetime import date

nascimento= int(input('digite o seu ano de nascimento '))
anoatual = date.today().year

idade = anoatual - nascimento
if idade <= 9:
    print('mirim')
elif idade <=14:
    print('infantil')    
elif idade <=19:
    print('junior')   
elif idade <=25:
    print('senior')       
else:
    print('master')       