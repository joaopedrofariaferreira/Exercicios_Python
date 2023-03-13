#Escrever um programa para aprovar um emprestimo bancario para compra de uma casa.
# o programa vai perguntar o valor da casa , o salario dop usuario e em quantos anos essa pessoa quer pagar
# calcule o valor da prestação mensal sendo que ela nao pode exceder 30% do salario. ou entao o emprestimo será negado
nome = input('Qual seu nome? ')
print(f'Seja bem vindo {nome}! Que legal saber que você quer comprar um imóvel. \n Irei te fazer algujmas perguntas agora!')
casa = float (input(f'Para começarmos, gostaria de saber qual o valor da casa {nome}? '))
salario = float (input('Qual o valor do seu sálario? '))
pagamento_anos  = int (input('Em quantos anos você gostaria de pagar seu imóvel?'))
if (casa / pagamento_anos) > (0.30 * salario):
    print('Infelizmentea a parcela do seu imóvel excede 30% do seu saário, talvez seja interessante juntar um pouco mais de dinheiro!')
else:
    print(f'Parabéns {nome}, você pode realizar esse investimento!')

