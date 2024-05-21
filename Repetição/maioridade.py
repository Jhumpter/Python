num = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da pessoa {}: '.format(c)))
    if idade >= 18:
        num += 1
if num == 0:
    print('Ninguém alcançou a maioridade')
elif num == 1:
    print('1 pessoa já alcançou a maioridade')
else:
    print('{} pessoas já alcançaram a maioridade'.format(num))
