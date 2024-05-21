frase = input('Digite uma frase: ').replace(' ', '')
inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
print(inverso)
