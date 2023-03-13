#construa um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome
# separadamente
# ex ana maira; primeiro: ana ; ultimo: maria
name = input('Digite seu nome: ')
#Dividindo o nome em blocos e removendo possiveis erros
name.strip()
#Dividindo o nome da pessoal em blocos
ultimo_nome = name.rsplit()
primeiro_nome = name.split()
str(print(f'O primeiro nome é {primeiro_nome[0]} e o seu ultimo nome é {ultimo_nome[-1]}'))


