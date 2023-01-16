import random
aluno1 = str(input('escreva o nome do primeiro aluno '))
aluno2 = str(input('escreva o nome do seg aluno '))
aluno3 = str(input('escreva o nome do ter aluno '))
aluno4 = str(input('escreva o nome do quar aluno '))


sorteado = (random.randint(1, 4))

if sorteado == 1: 
 print('o aluno sorteado foi {}'.format(aluno1) )

elif sorteado == 2:
 print('o aluno sorteado foi {}'.format(aluno2) )
elif sorteado == 3:
 print('o aluno sorteado foi {}'.format(aluno3) )
elif sorteado == 4:
 print('o aluno sorteado foi {}'.format(aluno4) )

else:
 print('erro')
