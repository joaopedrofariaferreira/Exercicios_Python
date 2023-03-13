#leia o prikmeiro termo
primeiro_termo = int(input("Digite o primeiro termos da PA: "))
#lendo a razao da pa
razao = int(input("Digite qual a razão da PA: "))
#mostrando os 10 primeiros termos
termo = primeiro_termo
resultado = 1
while resultado <=10:
    print(f"{termo}", end=' ')
    termo += razao
    resultado +=1
print('FIM')