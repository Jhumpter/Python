c = total = caro = menor = 0
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if c == 1:
        barato = produto
        menor = preco
    elif c != 1 and preco < menor:
        barato = produto
        menor = preco
    c += 1
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar != 'S':
        while continuar not in 'S,N':
            continuar = input('Valor inválido. Deseja continuar? [S/N]').strip().upper()[0]
print(f'''Dos {c} produtos: 
{caro} custam mais de R$1000,00,
{barato} é o mais barato, custando R${menor},
Foram gastos R${total}''')
