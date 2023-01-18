nome = str(input(' digite o seu nome '))

nome = nome.find('silva')

if nome == -1:
    print('não tem silva no seu nome')
else:
    print('existe silva no seu nome')    