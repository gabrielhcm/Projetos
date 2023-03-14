from random import randint
from time import sleep


dados = {'jogador1': randint(1,6),'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}

for j,c in dados.items():
    print(f"o {j} jogou o dado e tirou: {c}")
    sleep(1)
final = sorted(dados.items(),key=lambda res: res[1],reverse=True)    


print("Colocaçoes:")

for p, n in enumerate(final):
    print(f"{p+1} lugar: {n[0]} com {n[1]}.")