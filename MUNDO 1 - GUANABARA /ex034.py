#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salários superiores a 1250, calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%
nome = input('Qual seu nome? ')
salario = int(input(f'Quanto você ganha {nome}? '))
novo_salario = ((salario * 0.10) + salario)
novo_salario_15 = ((salario * 0.15) + salario)
if salario <= 1250:
    print(f'Parabéns {nome}, seu sálario será aumentado em 15%, agora você receberá {novo_salario_15}')
else:
    print(f'Parabéns {nome}, você recebeu um aumento de 10%, a partir de agora você ganhará {novo_salario}')
