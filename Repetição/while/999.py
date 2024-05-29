x = soma = c = 0
while x != 999:
    print('=-'*30)
    print('[999] para encerrar')
    x = int(input('Digite um número inteiro: '))
    soma += x
    c += 1
print('Foram digitados {} números'.format(c - 1))
print('A soma entre eles é {}'.format(soma - 999))
