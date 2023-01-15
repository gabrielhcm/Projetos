yuan = int(input('quanto você tem em yuan?'))
yen = int(input('quanto você tem em yen?'))
won = int(input('quanto você tem em won?'))

yuantotal  = yuan * 0.15
yentotal  = yen * 0.0076
wontotal  = won * 0.00081

somatotal = yuantotal + yentotal + wontotal


print(somatotal)