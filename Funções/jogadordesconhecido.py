def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gols')


n = input('Nome do jogador: ')
g = input('Número de gols: ')
if n == '':
    del n
if g == '':
    del g
ficha()
