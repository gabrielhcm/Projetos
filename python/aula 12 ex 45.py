import random
jogador= str(input('jokenpôoooo!!! '))


pcjoken = (random.randint(1,3))




if pcjoken == 1:
 pcescolha = 'pedra'
elif pcjoken == 2:
 pcescolha = 'papel'   
elif pcjoken == 3:
  pcescolha = 'tesoura'    

print(' o computador escolheu {}!'.format(pcescolha))

if jogador == 'pedra'and pcescolha == 'tesoura':
    print('pedra ganha de tesoura!')  
elif jogador == 'pedra' and pcescolha =='papel':
    print('papel ganha de pedra!')     
elif jogador == 'pedra' and pcescolha == 'pedra':  
     print('pedra empata com pedra!')  
elif jogador == 'papel' and pcescolha == 'papel':
    print('papel empata com papel!')       
elif jogador == 'papel' and pcescolha == 'pedra':
    print('papel ganha de pedra!')
elif jogador == 'papel' and pcescolha == 'tesoura':
    print('papel perde para tesoura')
elif jogador == 'tesoura' and pcescolha == 'tesoura':
    print('tesoura empata com tesoura')    
elif jogador == 'tesoura' and pcescolha == 'pedra':
    print('tesoura perde para pedra')     
elif jogador == 'tesoura' and pcescolha =='papel':
    print('tesoura ganha de papel')   






