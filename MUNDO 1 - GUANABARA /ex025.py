#crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome
nome = input('Digite seu nome: ')
print('Assumindo que 1 representa SIM e 0 representa NÃO')
print(f'a pessoal de nome {nome}, possui silva no nome? {nome.count("silva")}')
