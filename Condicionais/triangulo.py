n1 = float(input('Digite o 1º lado: '))
n2 = float(input('Digite o 2º lado: '))
n3 = float(input('Digite o 3º lado: '))
if (n1 + n2 >= n3) & (n2 + n3 >= n1) & (n1 + n3 >= n2):
    print('Pode ser um triângulo')
else:
    print('Não pode ser um triângulo')