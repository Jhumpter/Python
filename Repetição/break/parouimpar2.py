from random import randint
c = 0
while True:
    pc = randint(0,10)
    print('=-'*30)
    print('Par ou Ímpar!')
    n = int(input('Digite o valor: '))
    poui = (input('Par ou Impar? ')).strip().upper()[0]
    if (poui == 'P' and ((n + pc) % 2) == 0) or (poui == 'I' and ((n + pc) % 2) != 0):
        print('Você venceu!')
        print(f'O computador escolheu {pc} e você escolheu {n}')
        c += 1
    else:
        break
print(f'Perdeu! Você venceu {c} rodadas')
print(f'O computador escolheu {pc} e você escolheu {n}')
