# validaçao de dados com python
M = str('masculino')
F = str('Feminino')
#Recebendo resposta e tratando texto
pergunta = input('Qual seu sexo M / F? ').upper()
sexo = pergunta
#Montando a estrutura while adicionada de if para sempre repetir caso o ususario responda errado
'''while not sexo == M or F:
    input('Qual seu sexo M / F? ').upper()
    if sexo == M:
        print("Sua resposta foi para nosso banco de dados! ")
    elif sexo == F:
        print("Sua resposta foi para nosso banco de dados! ")
    else:
        input("Digite novamente sua resposta!\nQual SEU SEXO M / F")
print('Obrigado!')'''
#montando estrutura
while sexo not in 'MF':
    sexo = str(input("Qual o seu sexo M / F? ")).upper().strip()
print(f"Sexo {sexo} foi registrado com sucesso! ")