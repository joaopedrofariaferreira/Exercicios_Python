#Criar um programa que leia o cateto adjascente e o cateto oposto de um triangulo retangulo e nos de a hipotenusa
#sabemos que hipotenusa **2 é igual a cateto **2 mais cateto ao quaddrado, dessa forma
import math
cateto = int(input("Qual o cateto?" ))
cateto_oposto = int(input("Qual o cateto oposto? "))
hipotenusa = ((cateto**2) + (cateto_oposto**2))**0.5
print(f"A hipotenusa é igual a {hipotenusa}")
