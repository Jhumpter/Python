from random import randint
pc = randint(0, 10)
acertou = False
c = 0
while not acertou:
    usuario = int(input('Adivinhe o número de 0 a 10: '))
    c += 1
    if usuario == pc:
        acertou = True
    elif pc - 2 <= usuario <= pc + 2:
        print('Tá quente!')
    else:
        print('Tá frio!')
print('Acertou o número {} em {} tentativas'.format(pc, c))
