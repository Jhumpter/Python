times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')
input('Aperte "enter"')
print(f'''
No Brasileirão de 2023:
Os 5 primeiros colocados foram {times[:5]}
Os times rebaixados foram {times[-4:]}
Em ordem alfabética, os times foram {sorted(times)}
O Corinthians ficou na {times.index('Corinthians') + 1}ª posição
''')
