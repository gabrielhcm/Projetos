a = float(input('reta 1: '))
b = float(input('reta 2: '))
c = float(input('reta 3: '))



if( b - c ) < a < b + c and ( a - c ) < b < a + c and ( a - b ) < c < a + b:
   print( 'pode se formar um triangulo')
   
else:
  print('nao pode se formar um triangulo')

if a == b and b == c:
    print('equilatero')
elif a==b or a==c or b==c:
    print('isosceles')
elif a != b and b!=c:
    print('escaleno')    