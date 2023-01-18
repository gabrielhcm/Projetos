numero = int(input('digite um numero entre 0 e 9999 '))

u = numero // 1 % 10
d = numero // 10

print('você digitou o numero{} , que com os digitos separados são iguais a '.format(numero))

print(' unidade: {}'.format(u))
print('dezena: {}'.format(d))
