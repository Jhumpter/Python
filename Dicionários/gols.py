jogador = {'nome': input('Nome do jogador: ')}
gols = []
partidas = int(input('Quantas partidas foram jogadas? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {c}? ')))
print('=-'*30)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
for p, v in enumerate(gols):
    print(f'    =>Na partida {p+1} ele fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')
