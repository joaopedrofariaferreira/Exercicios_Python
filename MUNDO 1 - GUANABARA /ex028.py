#Escreva uma prgrama que faça o computador "pensar" um número inteiro entre 0 e 5 e peça para qo usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o suário
#venceu ou perdeu
from random import choice
n = [0, 1, 2, 3, 4, 5]
u = input('Qual seu nome usuário? ')
c = choice(n)
#pedindo para o usuário digitar um número
o = input(f'Agora digite um número de 0 a 5 {u}:')
if o == c:
    print(f'Parabéns {u} você acertou o número que eu estava pensando ')
else:
    print(f'Que pena {u} você errou! \n o número que eu escolhi foi {c}')
#fazendo o computador pensar um número
print(f'Olá usuário, o número que eu escolhi foi: {c}')
