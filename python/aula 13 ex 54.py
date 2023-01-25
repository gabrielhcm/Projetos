from datetime import date

anoatual = date.today().year

maioridade = 0
menoridade = 0






for pess in range(1,8):
    nasc = int (input('em que ano a {} pessoa nasceu?'.format(pess)))
    idade = anoatual - nasc
    if (anoatual - nasc) >=18:
        maioridade += 1
    else:
        menoridade+=1
print('{} pessoas atingiram a maior idade'.format(maioridade))
print('{} pessoas nao atingiram a maior idade'.format(menoridade))        











