#elabvore um program qua calcule um valor a ser pago por um prduto considerando seu preço normal e a condiçao de pagamento do produto
#avista no dinheiro ou cheque = ganha 10% de desconto
#a vista no cartao = 5% de desconto
#em até 2x no cartao = valor normal
#3x ou mais no cartao 20% de juros
valor_produto = float(input('Qual o valor do produto? R$ '))
dinheiro_cheque = float(valor_produto - (valor_produto * 0.10))
a_vista = float(valor_produto - (valor_produto * 0.05))
duas_vezes = float(valor_produto)
tres_ou_mais = float(valor_produto + (valor_produto * 0.20))
pagamento =int(input('Qual a forma de pagamento?\n [1- Dinheiro e cheque]\n [2- Á vista] \n [3- Parcelado em 2x]\n [4- Parcelado em 3x]'
                  '\n Inserir o metodo de pagamento: '))
if  pagamento == 1:
    print(f'Você selecionou o pagamento em Dinheiro / Cheque. O valor a ser pago pelo produto é de {dinheiro_cheque}!')
elif pagamento == 2:
    print(f'Você selecionou o pagamento á vista. O valor a ser pago pelo produto é de {a_vista}!')
elif pagamento == 3:
    print(f'Você selecionou o pagamento em 2X. O valor a ser pago é de {duas_vezes}!')
elif pagamento == 4:
    print(f'Você selecionou o pagamento em 3x ou mais. O valor a ser pago é de {tres_ou_mais}!')
else:
    print('Essa não é uma opção válida, tente novamente!')

