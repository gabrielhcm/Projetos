from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint (0,2)

print('''escolha uma opção: 
     [0] Pedra 
     [1] Papel
     [2] Tesoura
''')


jogador = int(input(' qual a sua jogada? '))

print('você jogou:{}!'.format(itens[jogador]))
print('o pc jogou:{}!'.format(itens[pc]))

if pc == 0:
 if jogador == 0:
  print('Empate!')
 elif jogador ==1:
  print(' você ganhou!')
 elif jogador == 2:
  print('Você perdeu')
 else:
    print('erro')   

elif pc ==1:
    if jogador ==1:
      print('Empate!')    
    elif jogador == 2:
      print('Você perdeu!') 
    elif jogador == 0:
     print('Você ganhou!')
    else:
     print('erro')     
elif pc ==2:
    if jogador == 2:
     print('Empate!')   
    elif jogador == 0:
     print('Você ganhou!')
    elif jogador == 1:
     print('Você perdeu')
    else:
     print('erro')   
else:
   print('erro')
 