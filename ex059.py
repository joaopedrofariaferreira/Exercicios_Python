'''valor_1=int(input("Olá usuario, digite o primeiro valor: "))
valor_2=int(input("Agora digite o segundo valor: "))
multiplicacao = int(valor_1 * valor_2)
print(multiplicacao)
divisao = int(valor_1 // valor_2)
print(divisao)
adicao = int(valor_1 + valor_2)
print(adicao)
subtracao = int(valor_1 - valor_2)
print(subtracao)
opcao_usuario = int(input("Digite qual sua opção:\n""1 - MULTIPLICAÇÃO \n""2 - DIVISÃO \n""3 - ADIÇÃO \n""4 - SUBTRAÇÃO \n"))
if opcao_usuario == 1:
    print(multiplicacao)
elif opcao_usuario == 2:
    print(divisao)
elif opcao_usuario == 3:
    print(adicao)
elif opcao_usuario == 4:
    print(subtracao)'''

'''valor_1=int(input("Olá usuario, digite o primeiro valor: "))
valor_2=int(input("Agora digite o segundo valor: "))
multiplicacao = int(valor_1 * valor_2)
print(multiplicacao)
divisao = int(valor_1 // valor_2)
print(divisao)
adicao = int(valor_1 + valor_2)
print(adicao)
subtracao = int(valor_1 - valor_2)
print(subtracao)
opcao_usuario = int(input("Digite qual sua opção:\n""1 - MULTIPLICAÇÃO \n""2 - DIVISÃO \n""3 - ADIÇÃO \n""4 - SUBTRAÇÃO \n""5 - FINALIZAR\n"))
while not opcao_usuario != 5:
    if opcao_usuario == 1:
        print(multiplicacao)
    elif opcao_usuario == 2:
        print(divisao)
    elif opcao_usuario == 3:
        print(adicao)
    elif opcao_usuario == 4:
        print(subtracao)
    else:
        break
print('fim')'''

opcao_usuario = 0
while opcao_usuario != 5:
    valor_1 = int(input("Olá usuario, digite o primeiro valor: "))
    valor_2 = int(input("Agora digite o segundo valor: "))
    opcao_usuario = int(input('Qual das opções gostaria:\n'
                              '1 - MULTIPLICAÇÃO\n'
                              '2 - DIVISÃO\n'
                              '3 - ADIÇÃO\n'
                              '4 - SUBTRAÇÃO\n'
                              '5 - FINALIZAR\n'
                              'Respostas: '))
    if opcao_usuario == 1:
        print(valor_1 * valor_2)
    elif opcao_usuario == 2:
        print(valor_1 // valor_2)
    elif opcao_usuario == 3:
        print(valor_1 + valor_2)
    elif opcao_usuario == 4:
        print(valor_1 - valor_2)
    elif opcao_usuario == 5:
        break
print('fim')