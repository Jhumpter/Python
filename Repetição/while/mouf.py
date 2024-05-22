sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Valor inválido! Tente novamente: ').strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
