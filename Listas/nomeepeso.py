pessoa = []
peso = []
cadastro = []
pesado = []
leve = []
for cont in range(0, 5):
    pessoa.append(input('Nome: '))
    peso.append(float(input('Peso: ')))
    cadastro.append([pessoa[-1], peso[-1]])
print(f'{len(pessoa)} pessoas foram cadastradas')
for p, v in enumerate(peso):
    if v == max(peso):
        pesado.append(pessoa[p])
    if v == min(peso):
        leve.append(pessoa[p])
print(f'O maior peso foi {max(peso):.2f}Kg, registrado por {pesado}')
print(f'O menor peso foi {min(peso):.2f}Kg, registrado por {leve}')
