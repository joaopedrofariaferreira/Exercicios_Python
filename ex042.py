#refazer o desafio 035 do mundo 1 acrescentando o recurso: mostrar qual o tipo de triangulo que será formado
#quilatero = todos os lados iguais
#isóceles = dois lados iguais
#escaleno = todos os lados diferentes
hipotenusa = int(input('Qual a medida do maior lado do triângulo? '))
cateto_oposto = int(input('Qual a medida do menor lado do triângulo? '))
cateto_adjascente = int(input('Qual a media do outro menor lado do triângulo? '))
soma_dos_catetos = int(cateto_adjascente + cateto_oposto)
cateto_oposto_e_hipotenusa = int(cateto_oposto + hipotenusa)
cateto_adjascente_e_hipotenusa = int(cateto_adjascente + hipotenusa)
if soma_dos_catetos > hipotenusa and cateto_oposto_e_hipotenusa > cateto_adjascente and cateto_adjascente_e_hipotenusa > cateto_adjascente:
    print('O triângulo pode existir!')
    if hipotenusa == cateto_oposto == cateto_adjascente:
        print('O triangulo é Equilatero')
    elif hipotenusa != cateto_oposto and cateto_oposto != cateto_adjascente and hipotenusa != cateto_adjascente:
        print('O triangulo é Escaleno')
    else:
        print('O triangulo  é Isoceles')
else:
    print('O triângulo não pode existeir')
