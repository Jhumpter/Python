n1 = int(input('Digite a nota na primeira prova: '))
n2 = int(input('Digite a nota na segunda prova: '))
media = (n1+n2)/2
if media < 5:
    print('\033[7;41mREPROVADO\033[m')
elif 5 == media < 6:
    print('\033[7;43mRECUPERAÇÃO\033[m')
elif media >= 6:
    print('\033[7;42mAPROVADO\033[m')
