qtde = int(input('Quantas pessoas serão cadastradas? '))
pessoas = []
cadastro = {}
for c in range(1, qtde+1):
    cadastro = {'nome': input('Nome: '),
                'sexo': input('Sexo(M/F): ').upper().strip()[0],
                'idade': int(input('Idade: '))}
    pessoas.append(cadastro.copy())
    cadastro.clear()
print(f'Foram cadastradas {qtde} pessoas')
media = 0
for v in pessoas:
    media += v['idade']
media /= qtde
print(f'A média das idades é {media}')
print('As mulheres são:')
for v in pessoas:
    if v['sexo'] == 'F':
        print(v)
print('As pessoas acima da média são:')
for v in pessoas:
    if v['idade'] > media:
        print(v)
