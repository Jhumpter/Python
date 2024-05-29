from Projeto_Cadastro.Arquivo import funcoes
def linha():
    print('-' * 30)
def res(n):
    while n not in '123' or n == '':
        n = input('\033[31mERRO! Tente novamente: \033[m')
    if n == '1':
        linha()
        print('{:^30}'.format('Pessoas Cadastradas'))
        linha()
        funcoes.mostrar()
    if n == '2':
        linha()
        print('{:^30}'.format('Nova pessoa'))
        linha()
        nome = input('Nome: ')
        idade = input('Idade: ')
        funcoes.adicionar(nome, idade)
    if n == '3':
        linha()
        print('{:^30}'.format('Finalizando programa'))
        linha()
        exit()
def menu():
    linha()
    print('{:^30}'.format('Menu Principal'))
    linha()
    print('''\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m
\033[33m3\033[m - \033[34mFechar programa\033[m''')
    linha()
    op = input('Digite uma das opções acima: ')
    return op