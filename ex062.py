#leia o prikmeiro termo
primeiro_termo = int(input("Digite o primeiro termos da PA: "))
#lendo a razao da pa
razao = int(input("Digite qual a razão da PA: "))
#mostrando os 10 primeiros termos
termo = primeiro_termo
resultado = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while resultado <= total:
            print(f"{termo}", end=' ')
            termo = termo + razao
            resultado +=1
    print( 'Pausa')
    mais = int(input('Quantos termos voce quer ver a mais?'))
print('FIM')