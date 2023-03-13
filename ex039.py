#faça um proigrama que leia a idade de um jovem e baseado nela diga se:
#ele ainda vai se alistar o serviço militar
#se é a hora dele se alistar no serviço militar
#já passou o tempo do alistamento militar
# o prgrama devera mostrar o tempo que falta ou que passou do alistamento
nome = input('Qual seu  nome? ')
idade = int(input('Qual a sua idade? '))
if idade > 18:
    print('já passou a hora do serviço militar, entre em contato para normalizar sua situação!')
elif idade == 18:
    print(f'Ainda da tempo de se alistar {nome}!')
else:
    print(f'Que bacana o interesse {nome}, quando fizer 18 anos, será sua hora!')
