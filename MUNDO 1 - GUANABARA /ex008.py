#Escrever um programa que leia em Metros e transforme para centimentros e milimetro
medida_metros = float(input("Qual a aprimeira medida em metros?"))
#Transformando a medida em metros para centimetros
medida_centimetros = float(medida_metros * 100)
medida_milimetros = float(medida_metros * 1000)
medida_decimetros = float(medida_metros * 10)
medida_decametros = float(medida_metros / 10)
medida_hectametro = float(medida_metros / 100)
medida_quilometros = float(medida_metros / 1000)
#Apresentando para o usuário
print(f"O valor da medida em centimetros é igual a {medida_centimetros} \n" 
      f"O valor da segunda medida em milimetros é igual a {medida_milimetros} \n"
      f"O valor da medida em Decimentros é igual a {medida_decimetros} \n"
      f"O valor da medida em Decametros é igual a {medida_decametros} \n"
      f"O valor da medida em Hectometros é igual a {medida_hectametro} \n"
      f"Ovalor da medida em Quilômetros é igual a {medida_quilometros}")
