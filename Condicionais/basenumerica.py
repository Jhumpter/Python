print('\033[7m1 para binário \033[m|\033[44m 2 para octal \033[m|\033[45m 3 para hexadecimal\033[m')
base = int(input('Escolha a base: '))
num = int(input('Digite o número a ser convertido: '))
if base == 1:
    print('Na base binária, o número {} fica {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('Na base octal, o número {} fica {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('Na base hexadecimal, o número {} fica {}'.format(num, hex(num)[2:]))
