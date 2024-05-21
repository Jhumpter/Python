import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))
