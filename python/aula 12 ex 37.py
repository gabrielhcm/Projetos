numer = int(input('digite um numero inteiro '))
opcao = int(input('escolha uma opção '))

conversao = 0

if opcao == 1:
 conversao = bin(numer)
 print('o numero convertido para bin fica: {}'.format(conversao))
elif opcao == 2:
 conversao = oct(numer)
 print('o numero convertido para oct fica: {}'.format(conversao))
elif opcao == 3:
 conversao = hex(numer)
 print(' o numero convertido para hex fica: {}'.format(conversao))