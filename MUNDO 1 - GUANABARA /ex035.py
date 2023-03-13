#desenvolva um programa que leia o comprimeto de 3 retas e diga ao usuario se ele pode ou nao formar um triangulo

#condicao de existencia triangulo
#Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado,
#então, a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado
hipotenusa = int(input('Qual a medida do maior lado do triângulo? '))
cateto_oposto = int(input('Qual a medida do menor lado do triângulo? '))
cateto_adjascente = int(input('Qual a media do outro menor lado do triângulo? '))
soma_dos_catetos = int(cateto_adjascente + cateto_oposto)
cateto_oposto_e_hipotenusa = int(cateto_oposto + hipotenusa)
cateto_adjascente_e_hipotenusa = int(cateto_adjascente + hipotenusa)
if soma_dos_catetos > hipotenusa and cateto_oposto_e_hipotenusa > cateto_adjascente and cateto_adjascente_e_hipotenusa > cateto_adjascente:
    print('O triângulo pode existir!')
else:
    print('O triângulo não pode existeir')
