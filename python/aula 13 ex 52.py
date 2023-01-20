num = int(input('digite um numero'))
total = 0
for c in range ( 1, num +1):
    if num % c ==0:
     print('\033[33m',end= ' ')  
    total += 1
print('{}'.format(c))