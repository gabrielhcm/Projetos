numero = int(input('digite um numero entre 0 e 9999 '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 
print('você digitou o numero{} , que com os digitos separados são iguais a '.format(numero))

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print ('centena: {}'.format(c))
print('milhar: {}'.format(m))