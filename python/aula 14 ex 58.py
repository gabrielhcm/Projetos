import random
numdig = 0
numeropc = (random.randint(1,11))
numetotent = 1

while numdig != numeropc:
    numdig = int(input('tente adivinhar o numero que o computador pensou! apenas numeros inteiros '))
    if numdig != numeropc:
        numetotent+= 1
        print('você não acertou o numero:( tenter novamente!')
print('você a certou o numero que o pc pensou que foi {} e você tentou {} vezes!'.format(numeropc, numetotent))        



