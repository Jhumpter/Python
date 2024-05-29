n = int(input('Elementos da sequência de Fibonacci: '))
c = 3
a1 = 1
a2 = 1
if n == 1:
    print(a1)
elif n == 2:
    print(a1, a2)
elif n > 2:
    print(a1, a2, end=' ')
    while c <= n:
        a3 = a1 + a2
        print(a3, end=' ')
        a1 = a2
        a2 = a3
        c += 1
