vsoma = 0
vtotal = 0
v3 = 0

v1 = int(input('digite o primeiro valor '))
v2 = int(input('digite o segundo valor  '))
while v3 != 5:
        print ('''[1] Somar
[2] multiplicar
[3] maior   
[4] novos numeros
[5] sair do programa''')
        v3 = int(input('qual a sua opção? '))     
        if v3 == 2:
                vsoma = v1*v2                     
                print(' {} multiplicado por {} é {}!'.format(v1,v2,vsoma))
        if v3 == 3:
                if v1>v2:
                        print('{} é maior que {}.'.format(v1, v2))
                else:
                        print('{} é maior que {}.'.format(v2,v1))

        if v3 == 1:
                vtotal = v1+v2
                print('{} + {} é: {} !'.format(v1,v2,vtotal))
        if v3 == 4:
                print('digite os numeros novamente!')
                v1 = int(input('digite o primeiro valor '))
                v2 = int(input('digite o segundo valor  '))        
print('fim do programa!')