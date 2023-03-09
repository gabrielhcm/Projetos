cha = int(input(''))
escolhas = list()
contador = 0
esc = list(str(input('')))
escolhas.append(esc)

for c in esc:
    if c ==" ":
        esc.remove(" ")

for c in esc:
    if c == str(cha):
        contador += 1  

print(contador)