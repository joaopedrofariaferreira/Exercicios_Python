#fazer um programa que leia a altura e largura de uma parede em metros e calcule sua área e o quanto de tina será utilizado
#cada galao de tinta consegue pintar 2 metros de paredela
largura = int(input("Qual a largura da sua parede? "))
altura = int(input("Qual a altura da sua parede? "))
#criando as variaveis do cálculo
area = int(largura * altura)
tinta = area/2
print(f"A sua parede possui {area} M2 de área, para esse tamanho de parede, será necessário utilizar {tinta} litros de tinta")


