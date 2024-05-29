while True:
    print('-'*30)
    print('Número negativo para finalizar')
    n = int(input('Tabuada do número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n}')
print('Tabuada encerrada')