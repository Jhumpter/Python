frase = input('Digite uma frase (sem acentos): ')
frase = frase.replace(' ', '').lower()
controle = 0
for c in range(0, (len(frase))//2):
    ultimo = len(frase) - 1 - c
    if frase[0 + c] == frase[ultimo]:
        controle += 0
    else:
        controle += 1
if controle == 0:
    print('Palíndromo')
else:
    print('Não é palíndromo')
