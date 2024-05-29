a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = coluna3 = 0
for c in range(0, 3):
    for m in range(0, 3):
        a[c][m] = int(input(f'Digite um valor para [{c+1}, {m+1}]: '))
for c in range(0, 3):
    for m in range(0, 3):
        print(f'[{a[c][m]:^5}]', end='')
        if (a[c][m] % 2) == 0:
            par += a[c][m]
    coluna3 += a[c][2]
    print()
linha2 = max(a[1])
print(f'A soma dos pares é {par}')
print(f'A soma dos termos da 3ª coluna é {coluna3}')
print(f'O maior valor da 2ª linha é {linha2}')
