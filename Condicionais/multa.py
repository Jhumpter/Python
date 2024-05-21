vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você ultrapassou a velocidade da via!')
    print('A multa é de R${:.2f}'.format((vel-80)*7))
