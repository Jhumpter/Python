from datetime import date
pessoa = {'Nome': input('Nome: '), 'Idade': date.today().year - int(input('Ano de nascimento: ')),
          'CTPS': int(input('Carteira de Trabalho (0 se não tiver): '))}
if pessoa['CTPS'] == 0:
    print(f'Nome: {pessoa['Nome']}\nIdade: {pessoa['Idade']}\nSem Carteira de Trabalho')
else:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    if date.today().year - pessoa['Ano de contratação'] > 35:
        pessoa['Aposentado'] = 'Sim'
    else:
        pessoa['Aposentado'] = 'Não'
    for k, v in pessoa.items():
        print(f'\033[35m{k}:\033[m {v}')
