#crie um programa que leia um numero inteiro qualquer e diga se ele é par ou impar
numero = int(input('Digite um número inteirop para saber se ele é ímppar ou par: '))
if (numero % 2) == 0:
    print('O número é divisivel por 2 logo é par')
else:
    print('O número não é divisivel por 2 logo ele é impar!')
