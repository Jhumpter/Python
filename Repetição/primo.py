n = int(input('Número testado: '))
controle = 0
for c in range(1, n):
    if (n % c) == 0 and c != 1:
        controle += 1
    elif (n % c) != 0:
        controle += 0
if controle != 0:
    print('Não é primo')
else:
    print('É primo')
