n = int(input('Digite um número para ver seu respectivo fatorial: '))
fat = 1
c = 0
while c != n:
    if c == 0:
        print('{}! = '.format(n), end='')
    print(n - c, end=' ')
    if n - c > 1:
        print('X', end=' ')
    fat *= n-c
    c += 1
print('= {}'.format(fat))
