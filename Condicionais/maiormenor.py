n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n3 > n2:
    aux = n2
    n2 = n3
    n3 = aux
if n2 > n1:
    aux = n1
    n1 = n2
    n2 = aux
if n3 > n2:
    aux = n2
    n2 = n3
    n3 = aux
print('O maior valor é {}'.format(n1))
print('O menor valor é {}'.format(n3))
