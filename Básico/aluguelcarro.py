import math
Km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
print('O aluguel custará R${:.2f}'.format(60*dias+Km*0.15))
