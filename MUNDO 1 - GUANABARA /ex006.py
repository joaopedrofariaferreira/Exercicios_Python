VAR1 = int(input("Digite um número"))
VAR2 = int(VAR1 * 2)
VAR3 = int(VAR1 ** 1/2)
print(f"O dobro do valor digitado é igual a {VAR2}", f"E a raiz quadrada é igual a {VAR3}")

#Prgrama para calcular a media de um aluno
VAR0 = input("Qual seu nome? ")
VAR1 = int(input("Qual foi sua primeira nota? "))
VAR2 = int(input("Qual foi sua segunda nota? "))
#CALCULANDO A MÉDIA DO ALUNO
VAR3 = (VAR1 + VAR2)/2
print(VAR0, f", sua média esse semestre foi de: {VAR3} pontos")

#Escrever um programa que leia em Metros e transforme para centimentros e milimetro
medida_metros = float(input("Qual a aprimeira medida em metros?"))
#Transformando a medida em metros para centimetros
medida_centimetros = float(medida_metros * 100)
medida_milimetros = float(medida_metros * 1000)
medida_decimetros = float(medida_metros * 10)
medida_decametros = float(medida_metros / 10)
medida_hectametro = float(medida_metros / 100)
medida_quilometros = float(medida_metros / 1000)
#Apresentando para o usuário
print(f"O valor da medida em centimetros é igual a {medida_centimetros} \n" 
      f"O valor da segunda medida em milimetros é igual a {medida_milimetros} \n"
      f"O valor da medida em Decimentros é igual a {medida_decimetros} \n"
      f"O valor da medida em Decametros é igual a {medida_decametros} \n"
      f"O valor da medida em Hectometros é igual a {medida_hectametro} \n"
      f"Ovalor da medida em Quilômetros é igual a {medida_quilometros}")

#Tabuada de qualquer numero
VAR1 = int(input("Digite um numero que você queira descobrir a tabuada: "))
print(f"{VAR1} x {1} = {VAR1*1}")
print(f"{VAR1} x {2} = {VAR1*2}")
print(f"{VAR1} x {3} = {VAR1*3}")
print(f"{VAR1} X {4} = {VAR1*4}")
print(f"{VAR1} X {5} = {VAR1*5}")
print(f"{VAR1} x {6} = {VAR1*6}")
print(f"{VAR1} x {7} = {VAR1*7}")
print(f"{VAR1} X {8} = {VAR1*8}")
print(f"{VAR1} x {9} = {VAR1*9}")
print(f"{VAR1} x {10} = {VAR1*10}")

#Programa que transforma o valor disponivel em dollar (fazer a conversão)
dinheiro = float( input("Quantos reais você tem? "))
dinheiro_convertido = float(dinheiro * 4.67)
print(f"Você possui um total de, {dinheiro_convertido} Dóllares!")

#fazer um programa que leia a altura e largura de uma parede em metros e calcule sua área e o quanto de tina será utilizado
#cada galao de tinta consegue pintar 2 metros de paredela
largura = int(input("Qual a largura da sua parede? "))
altura = int(input("Qual a altura da sua parede? "))
#criando as variaveis do cálculo
area = int(largura * altura)
tinta = area/2
print(f"A sua parede possui {area} M2 de área, para esse tamanho de parede, será necessário utilizar {tinta} litros de tinta")

#algoritmo para pegar um preço e fazer dele 5% para dar de desconto
VAR1 = float (input ("Digite um número"))
VAR2 = float (VAR1 * (5/100))
print(f"O valor do descoto é igual a {VAR2}")

#pegar um sálario e dar 15% de auento. Exibir esse resultado com um comparativo!
NAME = input("Qual seu nome? ")
SAL = float(15000 * 0.15)
print(f"Olá, {NAME}, seu sálario hoje é de 15 Mil reais" '\n'
f" Gostáríamos de lhe dar um reajuste de 15%! Totalizando {SAL}")

#transformar temperaturas
celsius = float(input("Digite uma temperatura em graus celsius: "))
fahrenheit = float((celsius * 9)/5) + 32
print(f"O valor de graus celsius para fahrenheit é igual a: {fahrenheit}")

#escrever um programa que pergunte a quantidade de kilomentros rodados por um carro alugado e a quantidade de dias pelo
# qual o mesmo foi alugago. calcule o preço a pagar. sabendo que o carro custa R$ 60 reais o dia e R$ 0,15 centavos o
# km rodado
km = float(input("Quantos kilometros foram rodados? "))
day = float(input("Por quantos dias o carro foi alugado? "))
#Calculando o resultado
valor_km_day = (print(f"o valor a ser pago pelo carro é de {(km * 0.15)+(day * 60)} "))
