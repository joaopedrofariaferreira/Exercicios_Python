#desenvolva um programa que pergunte a distancia da viagem km. Calcule o preço da passagem, cobrando 0,50 por km para viagens até 200 km
#e 0,45 para viagens mais longas
distancia = (int(input('Qual a distância viajada?')))
m = (distancia - 200) * 0.50
n = (distancia - 200) * 0.45
if distancia < 200:
    print(f'A distância percorrida foi de {distancia}\n O valor a ser pago é de {m}')
else:
    print(f'A distância percorrida foi maior que 200 KM você deverá pagar {n} reais')

