carrov = float(input('digite a velocidade do carro '))

velocidadeacima = carrov - 80
preçomulta = velocidadeacima * 7

if carrov > 80:
    print('voce ultrapassou a velocidade de 80km e foi multado!')
    print('A sua multa irá custar R${:.2f} Reais '.format(preçomulta))
else:
    print('você está seguindo a velocidade correta! :)')    