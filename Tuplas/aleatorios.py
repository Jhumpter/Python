from random import randint
n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números escolhidos foram {n}')
n = sorted(n)
print(f'O menor número é {n[0]}, e o maior é {n[-1]}')
