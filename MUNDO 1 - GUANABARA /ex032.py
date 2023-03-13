#faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Digite um ano que você gostaria de saber se é bissexto!'))
if (ano % 400) == 0:
    print(f'o ano de {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
