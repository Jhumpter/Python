c = soma = 0
while True:
    print('-' * 40)
    print('[999] para finalizar')
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'A soma dos {c} valores é igual a {soma}')
