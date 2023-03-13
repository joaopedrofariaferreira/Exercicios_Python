#faça um prgrama que leia um numero inteiro e diga se ele é ou nao um numero primo
numero = int(input('Digitre um número para saber se ele é PRIMO ou NÃO PRIMO: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO Número {numero} é divisivel {tot} vezes')
if tot == 2:
    print('Ele é um número primro')
else:
    print('\033[31m''E por isso ele não é um número primo')

