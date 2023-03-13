'''x = 1
numero = 0
novo_numero =
numero_termos = int(input('Quantos termos você gostaria de mostrar? '))
print('=-=' * 20)'''
numero_termos = int(input("Digite quantos termos quer ver da sequencia de fibonacci"))
n = 0
primeiro_termo = 0
segundo_termo = 1
contador = 3
while contador <= numero_termos:
    terceiro_termo = primeiro_termo + segundo_termo
    print(f"{terceiro_termo}-",end= " ")
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador += 1
print('Fim ')