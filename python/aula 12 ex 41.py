from datetime import date

ano = int(input('digite o seu ano de nascimento '))
anoatual = date.today().year

idade = ano - anoatual

if idade >=0 and  idade <= 9:
    print('mirim')
elif idade >= 9 and idade <=14:
    print('infantil')    
elif idade >= 14 and idade <=19:
    print('junior')   
elif idade >= 19 and idade <=20:
    print('senior')       
elif idade >= 21:
    print('master')       