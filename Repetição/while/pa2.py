a0 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
c = 1
extra = 0
print('{:.0f}'.format(a0))
while c < 10:
    a0 += r
    print('{:.0f}'.format(a0))
    c += 1
while extra != -1:
    print('[-1] para finalizar')
    extra += int(input('Deseja mais quantos termos?'))
    while (c - 10) < extra:
        a0 += r
        print('{:.0f}'.format(a0))
        c += 1
