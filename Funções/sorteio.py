from random import randint


def sorteio(lista, i, f):
    for c in range(1, 6):
        lista.append(randint(i, f))
    print('Os números sorteados foram: {}'.format(lista))


def somaPar(lista):
    pares = 0
    for c in lista:
        if (c % 2) == 0:
            pares += c
    print('A soma dos números pares sorteados é {}'.format(pares))


numeros = []
sorteio(numeros, int(input('Digite o mínimo: ')), int(input('Digite o máximo: ')))
somaPar(numeros)