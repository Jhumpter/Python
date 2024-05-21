from datetime import date
ano = int(input('Informe o ano de nascimento:'))
idade = date.today().year - ano
if idade < 18:
    falta = 18 - idade
    print('\033[32mAinda não está na hora! Faltam {} anos.\033[m'.format(falta))
elif idade == 18:
    print('\033[33mEstá na hora de se alistar! Busque a junta mais próxima.\033[m')
elif idade > 18:
    passou = idade - 18
    print('\033[31mEspero que tenha se alistado! Passaram-se {} anos do prazo.\033[m'.format(passou))
