doc = open('cic.txt', 'rt')
doc = doc.read()
lista = []
doc = doc.split('/')
for c in doc:
    campos = [campo.strip() for campo in c.split(',')]
    lista.append(campos)
for c in lista:
    c[0] = float(c[2])
for c in sorted(lista, reverse=True):
    print(c[0], c[1])
