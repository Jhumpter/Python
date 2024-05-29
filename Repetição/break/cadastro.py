h = m = adulto = c = 0
while True:
    print('='*10)
    print('CADASTRE UMA PESSOA')
    print('='*10)
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    idade = int(input('Idade: '))
    if idade >= 18:
        adulto += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    c += 1
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Dos {c} indivíduos cadastrados, {adulto} são maiores de idade, {h} são homens e {m} são mulheres com menos de 20 anos')
