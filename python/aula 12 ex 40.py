nota1 = float(input('digite a primeira nota '))
nota2 = float(input('digite a segunda nota '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('reprovado')
elif media >= 5.0 and media <= 6.9:
    print(' recuperação')    
elif media >= 7.0:
    print('aprovado') 
