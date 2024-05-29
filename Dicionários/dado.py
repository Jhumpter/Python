from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
res = {'Jogador 1': 0, 'Jogador 2': 0, 'Jogador 3': 0, 'Jogador 4': 0}
for k in res.keys():
    res[k] = randint(1, 6)
    print(f'O {k} tirou {res[k]}')
    sleep(1)
print('Ranking dos jogadores:')
res = sorted(res.items(), key=itemgetter(1), reverse=True)
#res virou uma lista de tuplas
for p, v in enumerate(res):
    sleep(1)
    print(f'{p+1}º lugar: {v[0]} com {v[1]}')
