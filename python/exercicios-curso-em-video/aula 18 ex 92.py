from datetime import datetime
dados = dict()
dados['nome'] = str(input("digite o nome "))
nas = int(input("data de nascimento"))
idade = datetime.now().year - nas
dados['idade'] = idade
dados['carteira'] = int(input("digite os numeres da carteira de trabalho ou 0 caso nao tenha: "))


if dados['carteira'] !=0:

    dados['anocont'] = int(input("digite o ano de contratação: "))
    dados['salario'] = int(input("digite o seu salario: "))
    dados['aposentadoria'] = (dados['anocont'] - nas) + 35 +2000

print(f"nome tem valor {dados['nome']}")
print(f"idade tem valor {idade}")
print(f"ctps tem valor {dados['carteira']}")


if dados['carteira'] !=0:

    print(f"contratação tem valor {dados['anocont']}")
    print(f"salario tem valor: {dados['salario']}")
    print(f"data de aposentadoria: {dados['aposentadoria']}")

