n = int(input('Digite um número de 4 dígitos: '))
u = n % 10
d = n // 10 % 100
c = n // 100 % 1000
m = n // 1000 % 10000
print('''{}
Milhar: {}
Centena: {}
Dezena: {}
Unidade: {}'''.format(n, m, c, d, u))
