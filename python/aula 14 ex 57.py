sexo = str(input('digite o seu sexo f/m!: ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('digite o seu sexo denovo, dados invalidos:')).strip().upper()[0]

print('o sexo {} registrado com sucesso'.format(sexo))              