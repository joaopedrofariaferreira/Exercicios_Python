#escrevas um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao
#1 para binário; 2 para octal; 3 para hexadecimal

numero = int(input('Qual o número que você quer converter? '))
num = (print('''Olá usuário, para qual base você gostaria de transformar seu numero? '
 [ 1 ] Converter para binário
 [ 2 ] converter para octal
 [ 3 ] converter para hexadecimal 
 '''))
opcao = int(input('Digite a opção: '))
if  opcao == 1:
    print(f' convertendo o numero {numero} para BINÁRIO...', print(bin(numero)))
elif opcao ==2:
    print(f'Convertendo o número {numero} para OCTAL...'), print(oct(numero))
elif opcao ==3:
    print(f'Converttendo o número {numero} para HEXADECIMAL...'), print(hex(numero))
else:
    print('O número que você digitou não corresponde as nossas bases de conversão!')

#realizando os calculos baseado na posição do numero

