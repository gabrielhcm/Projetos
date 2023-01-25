mmenos = 0
somaidade = 0
mediaidade = 0
mvelho = 0
nomevelho = ''
for pess in range(1,5): #fazer 3 fors ?
    print('-------------------------------------------------------')
    nome = str(input('digite o nome da {} pessoa: '.format(pess))).strip()
    idade = int(input('digite a idade da {} pessoa: '.format(pess)))
    sexo = str(input('digite o sexo da {} pessoa: '.format(pess))).strip()
    
    somaidade += idade
    if pess >= 1 and sexo in 'Mm':
        mvelho = nome
        nomevelho = idade
    if idade < 20 and sexo in 'Ff':
        
        mmenos +=1

    if mvelho == 0 :
        mvelho = 'nenhum'

mediaidade = somaidade / 4

print(' o homem mais velho tem {} anos  e o nome dele é: {}'.format(nomevelho, mvelho))
print('a media de idade do grupo é {}'.format(mediaidade))
print('{} mulheres tem idade menor que 20'.format(mmenos))



    
    
    
    
    
    
