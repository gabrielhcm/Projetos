numer = int(input('digite um numero inteiro '))
opcao = int(input('''escolha uma opção: 
     [1] converter para binario  
     [2] converter para octal
     [3] converter para hexadecimal
'''))

conversao = 0

if opcao == 1:
 conversao = bin(numer)[2:]
 print('o numero convertido para bin fica: {}'.format(conversao))
elif opcao == 2:
 conversao = oct(numer) [2:]
 print('o numero convertido para oct fica: {}'.format(conversao))
elif opcao == 3:
 conversao = hex(numer) [2:]
 print(' o numero convertido para hex fica: {}'.format(conversao))
else:
     print('opçao invalida')