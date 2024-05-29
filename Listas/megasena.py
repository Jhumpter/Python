from random import randint
palpites = []
jogo = []
n = int(input('Quantos jogos serão gerados? '))
for c in range(1, n+1):
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            palpites.append(jogo[:])
            jogo.clear()
            break
for c in range(0, n):
    palpites[c].sort()
    print(f'{c+1}º jogo: {palpites[c]}')
