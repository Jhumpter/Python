casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
tempo = int(input('Em quantos anos será pago? '))
tempo = tempo * 12
mensal = casa / tempo
maximo = salario * 0.3
if mensal > maximo:
    print('\033[31mO empréstimo não foi liberado\033[m')
elif mensal <= maximo:
    print('\033[32mO empréstimo foi liberado\033[m')
