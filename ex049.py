#REFAZER EXERCICIO 009 mostrandfo a tabuada do numero que o usuario escolher, so que agora utilizando o laço for
VAR1 = int(input("Digite um numero que você queira descobrir a tabuada: "))
for c in range (1,11):
    print(f"{VAR1} x {c} = {VAR1*c}")