def maior(lista):
    print(f'O maior dos números é {max(lista)}')


c = ''
lista = []
while c != 'N':
    lista.append(int(input('Digite um número: ')))
    c = input('Deseja continuar [S/N]? ').strip().upper()[0]
maior(lista)
