nome0 = input('Nome: ')
idade0 = int(input('Idade: '))
sexo0 = input('Sexo (M/F): ').title()
soma = 0
anciao = ''
if sexo0 == 'M':
    anciao = nome0
mulheres = 0
if sexo0 == 'F' and idade0 < 20:
    mulheres += 1
for c in range(1, 4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').title()
    soma += idade
    if idade > idade0 and sexo == 'M':
        anciao = nome
    elif idade == idade0 and sexo == 'M':
        anciao = anciao + ', ' + nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
media = (soma + idade0)/4
print('A média das idades do grupo é {}'.format(media))
if anciao.count(',') == 0:
    print('O homem mais velho é {}'.format(anciao))
elif anciao.count(',') != 0:
    print('Os homens mais velhos são {}'.format(anciao))
if mulheres == 1:
    print('Há 1 mulher abaixo de 20 anos')
elif mulheres == 0 or mulheres > 1:
    print('Há {} mulheres abaixo de 20 anos'.format(mulheres))
