
maior = 0
menor = 0

for pess in range(1,6):
    peso = float(input('digite o peso da {} pessoa'.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi: {:.2f}'.format(maior))
print('o menor peso foi: {}'.format(menor))        