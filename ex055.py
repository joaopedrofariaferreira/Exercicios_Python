#fAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS E NO FINAL MOSTRE QUAIS FORAM OS MAIOR E O MENOR PESO LIDOS
maior = 0
menor = 0
for people in range (1, 6):
    peso = int(input(f'Qual o peso da {people} pessoa?'))
    if people == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} kg')
print(f'O menor peso foi de {menor} kg')
