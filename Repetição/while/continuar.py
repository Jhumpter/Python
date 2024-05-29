continuar = 'S'
c = maior = menor = 1
soma = media = 0
while continuar in 'S':
    n = int(input('Digite um número: '))
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    media = soma / c
    c += 1
    continuar = input('[S/N] Deseja continuar? ').strip().upper()[0]
    while continuar not in 'S,N':
        continuar = input('Valor inválido, tente novamente [S/N]: ').strip().upper()[0]
print('''Dos números digitados:
A média é {}
O maior é {}
O menor é {}'''.format(media, maior, menor))
