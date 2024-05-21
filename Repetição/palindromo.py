frase = input('Digite uma frase: ')
frase = frase.replace(' ', '').lower()
for c in range(0, int(len(frase)/2)):
    ultimo = int(len(frase) - c)
    if frase[0 - c] == frase[ultimo]:
        print('Palíndromo')
    else:
        print('Não é palíndromo')
