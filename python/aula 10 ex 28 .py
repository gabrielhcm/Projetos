import random
numdig = int(input('tente adivinhar o numero que o computador pensou! apenas numeros inteiros '))


numeropc = (random.randint(0,5))

if numeropc == numdig:
    print('Você acertou o numero que o pc pensou!')
elif numeropc != numdig:
    print('Você não acertou o numerp oque o pc pensou :(  o numero que o pc pensou foi {} '.format(numeropc))
elif numdig <5:
    print('você digitou um numero maior que 5')     
else:
    print('Você digitou algo errado!')
     