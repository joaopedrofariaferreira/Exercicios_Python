#criar um programa que leia o nome de uma cidaded e diga se ela começa ou nao com o nome santo
cidade = input('qual o nome da sua cidade? ')
existe = cidade.count('santo')
inicio = cidade.find('santo')
print('ASSUMINDO 1 COMO VERDADE \nE 2 COMO NÃO, TEMOS')
print(f'A cidade digitada possui santo no começo {existe}, onde começa {inicio}')
