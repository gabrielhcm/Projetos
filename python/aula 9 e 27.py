nomecom = str(input('Digite o seu nome completo '))

noemdiv = nomecom.split()

nomeult = nomecom.rsplit(' ',1 )[-1]

print('primeiro nome {}'.format(noemdiv[0]))

print('ultimo nome {}'.format(nomeult))



