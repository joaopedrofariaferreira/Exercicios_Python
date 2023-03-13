#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, e  mostre uma mensage dizendo que ele foi
#multado:
#a multa vai custar 7 reias por km acima do limite
from random import randint
velocidade = randint(0, 300)
multa = float((velocidade - 80)*7)
if velocidade > 80:
    print(f'Seu carro estava a uma velocidade de {velocidade} KM/H \nVocê deverrá pagar {multa}')
else:
    print('seu carro estava dentro da velocidade permitida, você não foi multado!')