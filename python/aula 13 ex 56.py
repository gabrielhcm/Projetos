mmenos = 0
somaidade = 0
idademaior = 0
mediaidade = 0
mvelho = 0
for pess in range(1,5): #fazer 3 fors ?
    nome = str(input('digite o nome da {} pessoa '.format(pess)))
    idade = int(input('digite a idade da {} pessoa '.format(pess)))
    sexo = str(input('digite o sexo da {} pessoa '.format(pess)))
    somaidade += idade
    if pess >= 1 and sexo == 'M':
        mvelho = nome
    if pess > 0 and sexo == 'F':
        mmenos = idade
    if idade < 20 and sexo == 'F':
        mmenos +1


mediaidade = somaidade / 4

print(' o nome do homem mais velho é{}'.format(mvelho))
print('a media de idade do grupo é{}'.format(mediaidade))
print('{} tem idade menor que 20'.format(mmenos))



    
    
    
    
    
    
"""if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi: {:.2f}'.format(maior))
print('o menor peso foi: {}'.format(menor))     """