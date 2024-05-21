nome = input('Digite o seu nome: ')
nome = nome.title()
M = nome.upper()
m = nome.lower()
comp = len(''.join(nome.split()))
prim = len(nome.split()[0])
print('''O seu nome, {},
em maísculo fica {},
em minúsculo fica {},
possui {} letras, sendo {} do primeiro nome.
'''.format(nome, M, m, comp, prim))
