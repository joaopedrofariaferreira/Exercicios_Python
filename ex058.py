from random import randint
computador = randint(0,10)
print('Olá sou o computador, e acebni de pensar em um numero entre 0 e 10, voce consegue descobrir?')
print(computador)
acertou = False
#PARA SABER QUANTAS VEZES O USUARIO TENTOU ATE DESCOBRIR
palpites = 0
while not acertou:
    jogador = int(input('Digite o número que eu pensei: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('É um número maior!')
        elif jogador > computador:
            print('É um número menor!')
print(f'acerto, mizeravi!\nVocê precisou de {palpites} palpites')
