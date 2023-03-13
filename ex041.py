## crie um programa quie leia o ano de nascimento de um atleta e o encaixe em uma categoria
#ate 9 anos =mirim
#ate 14 anos=infantil
#até 19 anos=junior
#ate 20 anos=senior
#acima = master
nome = input('Qual seu nome? ')
nascimento = int(input('Qual o seu ano de nascimento '))
idade = (2022 - nascimento)
if idade <= 9:
    print('você é considerado MIRIM!')
elif idade <= 14:
    print('você está na categoria INFANTIL!')
elif idade <= 19:
    print('Você está na categoria JUNIOR!')
elif idade <= 20:
    print('Você está na categoria SENIOR!')
else:
    print('Você está na categoria MESTRE!')
