import random
num = ['0', '1', '2', '3', '4', '5']
pc = random.choice(num)
pl = str(input('Adivinhe o número de 0 a 5: '))
if pc == pl:
    print('Parabéns! O número {} era o correto!'.format(pc))
else:
    print('Infelizmente o número {} não era o certo. O número era {}'.format(pl, pc))
