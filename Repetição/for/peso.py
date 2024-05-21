maior = float(input('Peso da 1ª pessoa: '))
menor = maior
for c in range(2, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso inserido foi {}, enquanto o menor foi {}'.format(maior, menor))
