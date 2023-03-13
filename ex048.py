#faça um programa que calcule a sooma entre todos os numeros impares que sap multiplos de 3 de 1 a 500
soma = 0
contador = 0
for c in range(0, 500, 3):
    if c % 2 >= 1:
        contador = contador + 1
        soma = soma + c
print(soma, contador)
# MONTANDO FORMA DE EXCLUSION PARA NUMEROS PARES
