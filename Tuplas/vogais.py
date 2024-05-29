palavra = ('Pedro', 'Paulo', 'Mateus', 'Paula', 'Bianca', 'Fernanda')
for p in palavra:
    print(f'\nNa palavra {p} temos as vogais ', end='')
    for l in p:
        if l in 'AaEeIiOoUu':
            print(l, end=' ')
