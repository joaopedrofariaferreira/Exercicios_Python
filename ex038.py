#escrever um programa que leia dois numeros inteiros e compare - os, mostrando na tela uma mensagem:
# o primeiro valor é maior
#o segubndo valor é menor
#nao existe valor maior. os dois sao iguais
x = int(input('digite um número '))
y = int(input('Digite outro  número '))
if x > y:
    print('o primeiro valor é maior!')
elif x == y:
    print('não existe valor maior, ambos são iguais!')
else:
    print('O segundo valor é maior!')