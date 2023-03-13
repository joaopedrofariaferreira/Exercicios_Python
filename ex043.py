#escrever um aplicativo que leia o peso e altura de uma pessoa e calcule seu imc e mostro o estatus da pessoal
#abaixo de 18,5 = abaixo do poeso
#entre 18.5 e 25 = peso ideal
#25 a 30 = sobrepeso
#30 a 40 = obesidade
#maior que 40 = obesidade morbida
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = float(peso / (altura ** 2))
print(imc)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal')
elif 25 < imc <= 30:
    print('Você está com sobrepeso')
elif 30 < imc <= 40:
    print('Você está obeso')
else:
    print('Você está com obesidade morbida!')
