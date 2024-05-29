p = []
i = []
for cont in range(0, 6):
    v = int(input('Valor: '))
    if (v % 2) == 0:
        p.append(v)
    else:
        i.append(v)
n = [p + i]
p.sort()
i.sort()
print(f'Dos números {n} digitados, {p} são os pares e {i} são os ímpares')
