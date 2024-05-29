n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um valor: ')))
    contiuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if contiuar == 'N':
        break
    while contiuar != 'S':
        contiuar = input('Valor inválido.\nDeseja continuar? [S/N] ').strip().upper()[0]
for c in n:
    if (c % 2) == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Dos números {n} digitados, {par} são os pares e {impar} são os ímpares')
