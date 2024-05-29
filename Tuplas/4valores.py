n = (int(input('1º valor: ')), int(input('2º valor: ')), int(input('3º valor: ')), int(input('4º valor: ')))
cont = 0
par = ''
print(f'Você digitou os valores {n}')
if n.count(9) != 0:
    print(f'O número 9 apareceu {n.count(9)} vezes')
else:
    print('O número 9 não apareceu nenhuma vez')
if n.count(3) != 0:
    print(f'O número 3 apareceu pela primeira vez na posição {n.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
for c in n:
    if (c % 2) == 0:
        c = str(c)
        par += c + ' '
    else:
        cont += 1
if cont == 4:
    print('Nenhum valor par foi digitado')
else:
    print(f'Os valores {par}são pares')
