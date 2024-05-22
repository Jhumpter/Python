from time import sleep
menu = '4'
n1 = 0
n2 = 0
while menu not in '5':
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print('''
    O que você quer fazer com esses dois números?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos número
    [5] Fechar programa''')
    menu = input()
    if menu == '1':
        print('A soma entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1 + n2))
    elif menu == '2':
        print('A múltiplicação entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1 * n2))
    elif menu == '3':
        if n1 > n2:
            print('O maior entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior entre {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n2))
        elif n1 == n2:
            print('{} e {} são iguais'.format(n1, n2))
print('---- Fechando ----')
print('----- .', end='')
sleep(1)
print(' . ', end='')
sleep(1)
print('. -----')
sleep(1)
print('Programa Fechado')
