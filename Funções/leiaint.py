def leiaint(n):
    while not n.isnumeric():
        n = input('\033[31mERRO! Tente novamente: \033[m')
    print(f'Você digitou o número {n}')


leiaint(input('Digite um número: '))
