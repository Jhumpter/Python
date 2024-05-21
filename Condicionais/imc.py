altura = float(input('Altura (m): '))
peso = float(input('Peso (Kg): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}. '.format(imc), end='')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade')
elif 40 <= imc:
    print('Você está em obesidade mórbida')
