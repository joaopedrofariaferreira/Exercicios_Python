# crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda nao atingiram a maioridade
# e quantas já sao maiores . MAIORIDADE MAIS QUE 21
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for people in range(1, 8):
    nasc =  int (input(f'Qual a data de nascimento da {people} pessoa '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Assim, temos {totmaior} pessoas com mais de 21 anos e {totmenor} pessoas com menos de 21 anos')
