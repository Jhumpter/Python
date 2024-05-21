n = float(input('Digite um número: '))
print('A tabuada desse número é:')
c = 0
while c < 11:
    print('\n {} x {} = {}'.format(c, n, n*c))
    c += 1
