p = int(input('Digite um número de 0 a 20: '))
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while p > 20 or p < 0:
    print('Tente novamente')
    p = int(input('Digite um número de 0 a 20: '))
print(f'Você digitou o número {n[p]}')
