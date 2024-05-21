from datetime import date
ano = int(input('Digite o ano de nascimento do aluno: '))
idade = date.today().year - ano
if idade <= 9:
    turma = 'Mirim'
elif idade <= 14:
    turma = 'Infantil'
elif idade <= 19:
    turma = 'Junior'
elif idade <= 25:
    turma = 'Sênior'
else:
    turma = 'Master'
print(turma)