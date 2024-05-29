boletim = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas = [n1, n2]
    boletim.append([nome, notas])
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*10)
print('Nº  Nome             Média')
for c in range(0, len(boletim)):
    nome = boletim[c][0]
    media = (boletim[c][1][0] + boletim[c][1][1])/2
    print(f'{c:<4}{nome:<18}{media}')
print('_'*20)
while True:
    n = int(input('Mostrar nota de qual aluno (Nº)? [999] para interromper: '))
    if n > len(boletim)-1:
        break
    print(f'As notas de {boletim[n][0]} foram: {boletim[n][1]}')
