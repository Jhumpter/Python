input('Digite "enter" pra começar:')
n = 0
for c in range(1, 500):
    if (c % 3) == 0 and (c % 2) != 0:
        n += c
print(n)
