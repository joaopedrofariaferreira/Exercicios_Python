#fazer exercicio que leia um numero de 0  a 9999 e mostre na tela cadda um dos digitos separados
#ex: 1834, tem 4 unidades; 3 dezenas; 3 centenas e 1 milha
numero = str(input('Digite um número: '))
#separando o número digitado em blocos
numero.split()
#criando váriaveis para encaixa-lo em alguma
#pedir para o computador dizer se sim ou não, trabalhar com
unidade = numero[3]
dezena =  numero[2]
centena = numero[1]
milhar = numero[0]
print(f'o número digitado, {numero}, possui {unidade} unidades, {dezena} dezenas, {centena} centenas e {milhar} milhares')
#o programa assim so serve se coloarmos 4 digitos, as soluçoes par isso seriam, 1 utilizar sempre 4 digitos, onde
#usariamos 0 para completar a sequencia, ou refazer o codigo dessa forma

num = int(input('Digite um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'Analisando seu número {num}, ele é composto por {uni} Unidades, {dez} dezenas, {cen} centenas e {mil} milhares ')