Weight = float(input('peso: '))
tipo = str(input('(L)bs or(k)g:'))


if tipo.upper() == "L":
  peso =  Weight / 2.2046226218
else:
  peso =  Weight * 2.2046226218    

print(f"You are {peso:.2f} o tipo e {tipo}")    