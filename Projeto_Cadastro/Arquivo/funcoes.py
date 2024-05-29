def criar():
    try:
        a = open('arquivo.txt', 'rt')
        a.close()
    except FileNotFoundError:
        a = open('arquivo.txt', 'wt+')
        a.close()
def mostrar():
    a = open('arquivo.txt', 'rt')
    print(a.read())
def adicionar(nome, idade):
    a = open('arquivo.txt', 'at')
    a.writelines(f'{nome:<20}{idade:>10}\n')