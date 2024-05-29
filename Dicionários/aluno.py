aluno = {'Nome': input('Nome do aluno: '), 'Média': float(input('Média do aluno: '))}
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
