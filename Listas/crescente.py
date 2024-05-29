n = []
while True:
    n.append(int(input('Digite um valor: ')))
    if n[-1] in n[:-1]:
        print(f'O valor {n[-1]} já foi adicionado e será desconsiderado')
        del n[-1]
    contiuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if contiuar == 'N':
        break
    while contiuar != 'S':
        contiuar = input('Valor inválido.\nDeseja continuar? [S/N] ').strip().upper()[0]
n.sort()
print(n)
