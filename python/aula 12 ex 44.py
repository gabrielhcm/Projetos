preçoc = float(input(' digite o preço total das compras!'))

print(''' escolha a forma de pagamento
         [1] a vista dinheiro ou cheque
         [2] a vista no cartão
         [3] em até 2x no cartão
         [4] 3x ou mais

''')
escolha = int(input())

preço1 = (preçoc*0.10) 
preço1final =  preçoc  - preço1

preço2 = (preçoc*0.05) 
preço2final =  preçoc -  preço2 

preço3 = (preçoc*0.20) + preçoc
preço3final = preço3   


if escolha == 1:
    print('o custo das suas compras foi: {}'.format(preço1final))
 
elif escolha ==2:
     print('o custo das suas compras foi: {}'.format(preço2final))

elif escolha ==3:  
    print('o custo das suas compras foi: {}'.format(preçoc))

elif escolha ==4: 

 print('o custo das suas compras foi: {}'.format(preço3final))