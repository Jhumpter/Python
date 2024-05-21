nome0 = input('Nome: ')
idade0 = int(input('Idade: '))
sexo0 = input('Sexo (M/F): ').capitalize()
soma = 0
anciao = ''
if sexo0 == 'M':
    anciao = nome0
mulheres = 0
if sexo0 == 'F' and idade0 > 20:
    mulheres += 1
for c in range(1, 5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    soma += idade
    if idade > idade0 and sexo == 'M':
        anciao = nome
    elif idade == idade0 and sexo == 'M':
        anciao += nome
    if sexo == 'F' and idade > 20:
        mulheres += 1
media = (soma + idade0)/5
print('A média das idades do grupo é {}'.format(media))
print('O homem mais velho é {}'.format(anciao))
