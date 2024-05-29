n = [int(input('Número: '))]
M = []
m = []
for c in range(1, 5):
    n.append(int(input('Número: ')))
for c, v in enumerate(n):
    if v == max(n):
        M.append(c)
    if v == min(n):
        m.append(c)
print(n)
print(f'Maior: {max(n)} na posição {M}')
print(f'Menor: {min(n)} na posição {m}')
