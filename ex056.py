#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#no final o programa deve mostrar a media de idade do gruipo, qual o nome do homeme mais velho e quantas mulheres tem menos dde 21 aNOS
somaidade = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0
for p in range (1, 5):
    print(f'----- {p} PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo Masculino ou Feminino? ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'mM' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 = tot_mulher20 + 1
media = somaidade / 4
print(f'A media de idade do grupo é de {media}')
print(f'O homem mais velho tem {maior_idade_homem} anos de idade e se chama {nome_velho}')
print(f'Ao todo sao {tot_mulher20} mulheres com menos de 20 anos')
# achando o hgomem mais velho