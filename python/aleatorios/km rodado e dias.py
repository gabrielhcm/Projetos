kmp = float(input('quantos quilometros foram percorridos?'))
dias = int(input('quantos dias o carro foi alugado?'))

#o carro custa R$60 por dia e R$0,15 por Km rodado.

kmpc = kmp * 0.15
diasc = dias * 60

print('você gastou {} por km rodados e {} por dias alugados , tendo que pagar um total de {:.2f}'.format(kmpc, diasc,kmpc + diasc ))