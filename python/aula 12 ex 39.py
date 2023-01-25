from datetime import date

ano = int(input('digite o seu ano de nascimento '))

anoatual = date.today().year

if (ano - anoatual) == 18:
    print('você precisa se alistar')
elif ano - anoatual < 18:
    print('já passou do ano de se alistar')    
elif ano - anoatual > 18:
    print('ainda está muito novo para se alistar')   