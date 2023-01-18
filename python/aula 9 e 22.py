nome = str(input('digite o seu nome completo')).strip()

nomesemes = nome.strip()

nomesplit = nome.split()

tamprinome = nomesplit[0]

print('o seu nome com as letras maiusculas é {}'.format (nome.upper()))
print('o seu nome com as letras minusculas é {}'.format (nome.lower()))
print(' o seu nome tem {} letras'.format(len(nomesemes)- nomesemes.count(' ')))
print (' o seu primeiro nome tem {} letras'.format(len(tamprinome)))
