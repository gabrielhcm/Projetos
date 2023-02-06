nome = str(input(' digite o seu nome ')).strip()

nome = nome.find('silva').upper()

if nome == -1:
    print('não tem silva no seu nome')
else:
    print('existe silva no seu nome')    