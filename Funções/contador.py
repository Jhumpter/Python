from time import sleep


def conte(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print(fim)
    print('Fim!')


print('Contando de 1 até 10: ')
conte(1, 10, 1)
print('Contando de 10 até 0 de 2 em 2: ')
conte(10, 0, -2)
conte(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
