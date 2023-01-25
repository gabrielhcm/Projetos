import random
pergunta = input('faça sua pergunta! ')

numerorandom = random.randint(1, 9)

print('Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk' )


if numerorandom == 1:

 resposta = 'Yes - definitely.'

elif numerorandom == 2:
 resposta = 'It is decidedly so'
elif numerorandom == 3:
 resposta = 'Without a doubt.'
elif numerorandom == 4:
 resposta = 'Reply hazy, try again.'
elif numerorandom == 5:
 resposta = 'Ask again later.'
elif numerorandom == 6:
 resposta = 'Better not tell you now.'
elif numerorandom == 7:
 resposta = 'My sources say no.'
elif numerorandom == 8:
 resposta = 'Outlook not so good.'
elif numerorandom == 9:
 resposta = 'Very doubtful.'

else:
 resposta == 'erro'

print('pergunta: ' + pergunta )
print ('magic 8 ball: ' + resposta)