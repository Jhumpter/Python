valor = int(input('Digite o valor a ser sacado: R$'))
c = v = d = u = 0
while True:
    if valor >= 50:
        c = valor // 50
        valor = valor % 50
    elif valor >= 20:
        v = valor // 20
        valor = valor % 20
    elif valor >= 10:
        d = valor // 10
        valor = valor % 10
    elif valor >= 1:
        u = valor // 1
        valor = valor % 1
    else:
        break
print(f'''Total de:
{c} cédulas de 50
{v} cédulas de 20
{d} cédulas de 10
{u} cédulas de 1''')
