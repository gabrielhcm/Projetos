from random import shuffle
aluno1 = str(input('escreva o nome do primeiro aluno '))
aluno2 = str(input('escreva o nome do seg aluno '))
aluno3 = str(input('escreva o nome do ter aluno '))
aluno4 = str(input('escreva o nome do quar aluno '))

lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)

print('o aluno escolhido foi {}'.format(lista))