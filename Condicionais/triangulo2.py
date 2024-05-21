n1 = float(input('Digite o 1º lado: '))
n2 = float(input('Digite o 2º lado: '))
n3 = float(input('Digite o 3º lado: '))
if (n1 + n2 >= n3) & (n2 + n3 >= n1) & (n1 + n3 >= n2):
    if n1 == n2 == n3:
        print('Pode ser um triângulo equilátero')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Pode ser um triângulo isósceles')
    else:
        print('Pode ser um triângulo escaleno')
else:
    print('Não pode ser um triângulo')
