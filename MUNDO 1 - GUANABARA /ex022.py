#criar um aplicativo que leia o nome completo de uma pessoa e mostra
#o nome com todas as letras maiusculas
nome = 'João Pedero de Faria Ferreira'
letras_maiusculas = nome.upper()
print(letras_maiusculas)
#o nome com todas as letras minusculas
letras_minusculas = nome.lower()
print(letras_minusculas)
#quantas letras ao todo sem considerar os espaços
espacos_vazios = nome.count(" ")
comprimento_frase = (print(f"A frase tem comprimento igual a {len(nome)}"))
print(f'Existem ao todo {espacos_vazios} espaços vazios')
#a quantidade de letras no primeiro nome
nome_separado = nome.split()
print(f'seu primeiro nome é "{nome_separado [0]}" e possui {len(nome_separado[0])} letras' )


